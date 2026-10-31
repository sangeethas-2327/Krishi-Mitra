import json
import sys
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(backend_dir))

from app.models.scheme import SchemeRecord
from app.data.schemes_central import get_central_schemes
from app.data.schemes_karnataka import get_karnataka_schemes
from app.data.schemes_demo import get_demo_schemes

def main():
    central = get_central_schemes()
    karnataka = get_karnataka_schemes()
    demo = get_demo_schemes()

    print(f"Loaded: {len(central)} Central, {len(karnataka)} Karnataka, {len(demo)} Demo schemes.")
    all_raw = central + karnataka + demo
    print(f"Total candidate schemes: {len(all_raw)}")

    validated_schemes = []
    seen_ids = set()

    for idx, raw in enumerate(all_raw):
        sid = raw.get("id")
        if not sid:
            raise ValueError(f"Scheme at index {idx} has no id!")
        if sid in seen_ids:
            raise ValueError(f"Duplicate scheme ID: {sid}")
        seen_ids.add(sid)

        # Validate with Pydantic model
        record = SchemeRecord.model_validate(raw)
        validated_schemes.append(record.model_dump(mode="json"))

    output_path = Path(__file__).resolve().parent / "schemes.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(validated_schemes, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Successfully validated and saved {len(validated_schemes)} schemes to {output_path}")

if __name__ == "__main__":
    main()

