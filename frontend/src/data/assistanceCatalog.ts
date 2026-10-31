export interface AssistanceItem {
  key: string;       // Normalized lowercase key e.g. "kcc_loan", "subsidy", "drip_irrigation"
  name_en: string;
  name_kn: string;
  description_en?: string;
  description_kn?: string;
}

export interface AssistanceCategory {
  id: string;
  name_en: string;
  name_kn: string;
  items: AssistanceItem[];
}

export const ASSISTANCE_CATEGORIES: AssistanceCategory[] = [
  {
    id: "credit_loans",
    name_en: "Credit & Financial Assistance",
    name_kn: "ಸಾಲ & ಹಣಕಾಸು ನೆರವು",
    items: [
      { key: "kcc_loan", name_en: "Kisan Credit Card (KCC) Crop Loan", name_kn: "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC) ಬೆಳೆ ಸಾಲ" },
      { key: "interest_subvention", name_en: "Interest Subvention / 0% Interest Loan", name_kn: "ಬಡ್ಡಿ ರಿಯಾಯಿತಿ / ಶೂನ್ಯ ಬಡ್ಡಿ ಸಾಲ" },
      { key: "term_loan", name_en: "Agricultural Term Loan / Equipment Loan", name_kn: "ಕೃಷಿ ಅವಧಿ ಸಾಲ / ಯಂತ್ರೋಪಕರಣ ಸಾಲ" },
      { key: "income_support", name_en: "Direct Income Support (PM-KISAN)", name_kn: "ನೇರ ನಗದು ನೆರವು (ಪಿಎಂ-ಕಿಸಾನ್)" },
      { key: "pension", name_en: "Farmer Pension Scheme (PM-KMY)", name_kn: "ರೈತ ಪಿಂಚಣಿ ಯೋಜನೆ (PM-KMY)" }
    ]
  },
  {
    id: "subsidies_grants",
    name_en: "Subsidies & Capital Grants",
    name_kn: "ಸಹಾಯಧನ & ಅನುದಾನ",
    items: [
      { key: "machinery_subsidy", name_en: "Farm Machinery Subsidy (SMAM)", name_kn: "ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಸಹಾಯಧನ (SMAM)" },
      { key: "horticulture_subsidy", name_en: "Horticulture Mission Grant (MIDH)", name_kn: "ತೋಟಗಾರಿಕೆ ಅಭಿವೃದ್ಧಿ ಸಹಾಯಧನ (MIDH)" },
      { key: "polyhouse_subsidy", name_en: "Polyhouse & Shade Net Subsidy", name_kn: "ಪಾಲಿಹೌಸ್ & ನೆರಳು ಪರದೆ ಸಹಾಯಧನ" },
      { key: "solar_pump_subsidy", name_en: "PM-KUSUM Solar Pump Subsidy", name_kn: "ಸೌರ ಪಂಪ್‌ಸೆಟ್ ಸಹಾಯಧನ (ಕುಸುಮ್)" },
      { key: "fencing_subsidy", name_en: "Solar Fencing & Crop Protection Subsidy", name_kn: "ಸೌರ ಬೇಲಿ & ಕಾಡುಪ್ರಾಣಿ ರಕ್ಷಣೆ ಸಹಾಯಧನ" }
    ]
  },
  {
    id: "irrigation",
    name_en: "Irrigation Facilities",
    name_kn: "ನೀರಾವರಿ ಸೌಲಭ್ಯಗಳು",
    items: [
      { key: "drip_irrigation", name_en: "Drip Irrigation Subsidy (PMKSY-PDMC)", name_kn: "ಹನಿ ನೀರಾವರಿ ಸಹಾಯಧನ (PMKSY-PDMC)" },
      { key: "sprinkler_irrigation", name_en: "Sprinkler Irrigation Facility", name_kn: "ತುಂತುರು ನೀರಾವರಿ ಸೌಲಭ್ಯ" },
      { key: "ganga_kalyana", name_en: "Ganga Kalyana Scheme (Borewell & Pump)", name_kn: "ಗಂಗಾ ಕಲ್ಯಾಣ ಕೊಳವೆಬಾವಿ ಯೋಜನೆ" },
      { key: "farm_pond", name_en: "Krishi Bhagya Farm Pond (Krishi Honda)", name_kn: "ಕೃಷಿ ಭಾಗ್ಯ ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ" },
      { key: "pipeline_subsidy", name_en: "Irrigation Pipeline Subsidy", name_kn: "ನೀರಾವರಿ ಪೈಪ್‌ಲೈನ್ ಸಹಾಯಧನ" }
    ]
  },
  {
    id: "crop_insurance",
    name_en: "Crop Insurance & Compensation",
    name_kn: "ಬೆಳೆ ವಿಮೆ & ನಷ್ಟ ಪರಿಹಾರ",
    items: [
      { key: "pmfby_insurance", name_en: "PM Fasal Bima Yojana (PMFBY)", name_kn: "ಪ್ರಧಾನ ಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ (PMFBY)" },
      { key: "rwbcis_insurance", name_en: "Weather-based Crop Insurance (RWBCIS)", name_kn: "ಹವಾಮಾನ ಆಧಾರಿತ ಬೆಳೆ ವಿಮೆ (RWBCIS)" },
      { key: "drought_compensation", name_en: "Drought / Flood Relief (NDRF/SDRF)", name_kn: "ಬರ / ಪ್ರವಾಹ ಪರಿಹಾರ (ಪರಿಹಾರ ತಂತ್ರಾಂಶ)" },
      { key: "pest_compensation", name_en: "Pest Attack & Disease Compensation", name_kn: "ಕೀಟಬಾಧೆ & ರೋಗ ನಷ್ಟ ಪರಿಹಾರ" }
    ]
  },
  {
    id: "mechanization",
    name_en: "Farm Mechanization & Tools",
    name_kn: "ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ & ಬಾಡಿಗೆ ಕೇಂದ್ರ",
    items: [
      { key: "tractor_subsidy", name_en: "Tractor & Power Tiller Subsidy", name_kn: "ಟ್ರ್ಯಾಕ್ಟರ್ & ಪವರ್ ಟಿಲ್ಲರ್ ಸಬ್ಸಿಡಿ" },
      { key: "drone_subsidy", name_en: "Agricultural Drone (Namo Drone Didi)", name_kn: "ಕೃಷಿ ಡ್ರೋನ್ ಸೌಲಭ್ಯ (ನಮೋ ಡ್ರೋನ್ ದೀದಿ)" },
      { key: "chc_rental", name_en: "Custom Hiring Centre (CHC) Rentals", name_kn: "ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಬಾಡಿಗೆ ಕೇಂದ್ರ (CHC)" },
      { key: "harvester_equipment", name_en: "Paddy / Sugarcane Harvester & Thresher", name_kn: "ಭತ್ತ / ಕಬ್ಬು ಕಟಾವು ಯಂತ್ರ & ಒಕ್ಕಣೆ ಉಪಕರಣ" },
      { key: "sprayers", name_en: "Power Sprayers & Weeders", name_kn: "ಪವರ್ ಸ್ಪ್ರೇಯರ್ & ಕಳೆ ಕೀಳುವ ಯಂತ್ರ" }
    ]
  },
  {
    id: "seeds_planting",
    name_en: "Seeds & Planting Material",
    name_kn: "ಬೀಜ & ಸಸಿಗಳು",
    items: [
      { key: "certified_seeds", name_en: "Subsidized Certified Hybrid Seeds", name_kn: "ರಿಯಾಯಿತಿ ದರದ ಪ್ರಮಾಣಿತ ಬಿತ್ತನೆ ಬೀಜ" },
      { key: "horticulture_saplings", name_en: "Quality Arecanut, Coconut & Fruit Saplings", name_kn: "ಅಡಿಕೆ, ತೆಂಗು & ಹಣ್ಣಿನ ಗುಣಮಟ್ಟದ ಸಸಿಗಳು" },
      { key: "seed_treatment", name_en: "Bio-fertilizer Seed Treatment Kits", name_kn: "ಜೈವಿಕ ಬೀಜೋಪಚಾರ ಕಿಟ್‌ಗಳು" }
    ]
  },
  {
    id: "soil_fertilizer",
    name_en: "Fertilizer & Soil Health",
    name_kn: "ರಸಗೊಬ್ಬರ & ಮಣ್ಣಿನ ಆರೋಗ್ಯ",
    items: [
      { key: "soil_health_card", name_en: "Soil Health Card & Soil Testing", name_kn: "ಮಣ್ಣು ಆರೋಗ್ಯ ಪತ್ರಿಕೆ (Soil Health Card)" },
      { key: "organic_farming", name_en: "PKVY Organic Farming & Vermicompost Subsidy", name_kn: "ಪರಂಪರಾಗತ್ ಸಾವಯವ ಕೃಷಿ & ಎರೆಹುಳು ಗೊಬ್ಬರ" },
      { key: "nano_fertilizer", name_en: "Nano Urea & Nano DAP Assistance", name_kn: "ನ್ಯಾನೋ ಯೂರಿಯಾ & ನ್ಯಾನೋ ಡಿಎಪಿ ನೆರವು" },
      { key: "micronutrients", name_en: "Micronutrient & Zinc Kits Subsidy", name_kn: "ಲಘು ಪೋಷಕಾಂಶ & ಸತುವಿನ ಕಿಟ್‌ಗಳು" }
    ]
  },
  {
    id: "storage_infrastructure",
    name_en: "Storage, Processing & Marketing",
    name_kn: "ದಾಸ್ತಾನು, ಸಂಸ್ಕರಣೆ & ಮಾರುಕಟ್ಟೆ",
    items: [
      { key: "aif_financing", name_en: "Agri Infrastructure Fund (AIF) Godown & Cold Storage", name_kn: "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (AIF) ಗೋದಾಮು & ಶೀತಲ ಕೇಂದ್ರ" },
      { key: "enam_access", name_en: "e-NAM National Agriculture Market Access", name_kn: "ಇ-ನ್ಯಾಮ್ (e-NAM) ಆನ್‌ಲೈನ್ ಮಾರುಕಟ್ಟೆ ಸಂಪರ್ಕ" },
      { key: "pacs_processing", name_en: "PACS Primary Processing & Grading Unit", name_kn: "ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘಗಳ ಸಂಸ್ಕರಣಾ ಘಟಕ" },
      { key: "drying_yard", name_en: "Crop Drying Yard (ಕಣ ನಿರ್ಮಾಣ)", name_kn: "ಕೃಷಿ ಉತ್ಪನ್ನ ಒಣಗಿಸುವ ಕಣ ನಿರ್ಮಾಣ" }
    ]
  },
  {
    id: "msp_procurement",
    name_en: "Minimum Support Price & Procurement",
    name_kn: "ಬೆಂಬಲ ಬೆಲೆ & ಸರ್ಕಾರಿ ಖರೀದಿ",
    items: [
      { key: "msp_procurement", name_en: "MSP Procurement Centres Registration", name_kn: "ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆ (MSP) ಖರೀದಿ ಕೇಂದ್ರ ನೋಂದಣಿ" },
      { key: "pm_aasha", name_en: "PM-AASHA Price Deficiency Support", name_kn: "ಪಿಎಂ-ಆಶಾ ಬೆಲೆ ಕೊರತೆ ಪರಿಹಾರ ಯೋಜನೆ" },
      { key: "market_intervention", name_en: "Market Intervention Scheme (MIS)", name_kn: "ಮಾರುಕಟ್ಟೆ ಮಧ್ಯಪ್ರವೇಶ ಯೋಜನೆ (MIS)" }
    ]
  },
  {
    id: "allied_activities",
    name_en: "Animal Husbandry & Allied Activities",
    name_kn: "ಪಶುಸಂಗೋಪನೆ & ಪೂರಕ ಚಟುವಟಿಕೆಗಳು",
    items: [
      { key: "dairy_subsidy", name_en: "Dairy Cattle / Buffalo Purchase Subsidy", name_kn: "ಹೈನುಗಾರಿಕೆ ಹಸು / ಎಮ್ಮೆ ಖರೀದಿ ಸಹಾಯಧನ" },
      { key: "cattle_shed", name_en: "MGNREGA Cattle Shed Construction (ದನದ ಕೊಟ್ಟಿಗೆ)", name_kn: "ನರೇಗಾ ದನದ ಕೊಟ್ಟಿಗೆ ನಿರ್ಮಾಣ" },
      { key: "sheep_goat", name_en: "Amritha Swabhimani Sheep & Goat Rearing", name_kn: "ಅಮೃತ ಸ್ವಾಭಿಮಾನಿ ಕುರಿ & ಮೇಕೆ ಸಾಕಾಣಿಕೆ" },
      { key: "fisheries", name_en: "PMMSY Fisheries & Fish Pond Subsidy", name_kn: "ಪ್ರಧಾನ ಮಂತ್ರಿ ಮತ್ಸ್ಯ ಸಂಪದ (PMMSY) ಮೀನುಗಾರಿಕೆ" }
    ]
  }
];

export function findAssistanceByKey(key: string): AssistanceItem | undefined {
  const normKey = key.trim().toLowerCase();
  for (const cat of ASSISTANCE_CATEGORIES) {
    const found = cat.items.find((i) => i.key === normKey);
    if (found) return found;
  }
  return undefined;
}

