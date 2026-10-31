import logging
from typing import List, Optional
from ..models.farmer import FarmerProfile
from ..models.scheme import SchemeMatchResult, SchemeStatus, SchemeRecord
from .scheme_source_service import SchemeSourceService
from .eligibility_engine import EligibilityEngine

logger = logging.getLogger(__name__)

CATEGORY_NEED_MAP = {
    "income_support": ["subsidy", "income_support", "support", "financial_aid"],
    "crop_insurance": ["insurance", "crop_insurance", "relief"],
    "irrigation": ["irrigation", "drip", "sprinkler", "water", "borewell", "subsidy"],
    "equipment": ["equipment", "machinery", "tools", "subsidy", "farm_mechanization"],
    "soil_health": ["soil_health", "fertilizer", "soil", "compost", "subsidy"]
}

class SchemeRecommender:
    @classmethod
    def get_recommendations(
        cls,
        profile: FarmerProfile,
        category: Optional[str] = None
    ) -> List[SchemeMatchResult]:
        schemes = SchemeSourceService.get_all()
        results: List[SchemeMatchResult] = []

        for scheme in schemes:
            if category and scheme.category != category:
                continue

            match_res = EligibilityEngine.evaluate_scheme(scheme, profile)
            results.append(match_res)

        # Transparent ranking logic
        def rank_key(res: SchemeMatchResult):
            # 1. Relevance to farmer's stated assistance needs
            relevance_boost = 0
            if profile.assistance_needs:
                target_needs = CATEGORY_NEED_MAP.get(res.scheme.category, [])
                overlap = set(profile.assistance_needs).intersection(set(target_needs))
                if overlap:
                    relevance_boost = 100

            # 2. Evaluation status weight
            status_weight = {
                SchemeStatus.POTENTIALLY_SUITABLE: 50,
                SchemeStatus.REQUIRES_OFFICIAL_VERIFICATION: 40,
                SchemeStatus.INSUFFICIENT_INFORMATION: 30,
                SchemeStatus.NOT_SUITABLE_BASED_ON_KNOWN_RULES: 0
            }.get(res.evaluation_status, 10)

            # 3. Real scheme preference over synthetic demo
            scheme_type_weight = 20 if res.scheme.scheme_type == "real" else 10

            # 4. Number of satisfied criteria
            satisfied_count = len(res.satisfied_rules)

            total_score = relevance_boost + status_weight + scheme_type_weight + satisfied_count
            return total_score

        # Sort descending by calculated score
        results.sort(key=rank_key, reverse=True)
        return results
