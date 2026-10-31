from pathlib import Path
import re

p = Path("backend/app/data/schemes_karnataka.py")
content = p.read_text(encoding="utf-8")

# In kmi_water:
# make_rule("kmi_water", "Must possess an assured water source (Borewell, Open well, River/Canal lifting).", "ಸುಸ್ಥಿರ ನೀರಿನ ಮೂಲ (ಬೋರ್‌ವೆಲ್, ತೆರೆದ ಬಾವಿ ಅಥವಾ ನದಿ ಮೂಲ) ಹೊಂದಿರಬೇಕು.", "irrigation.has_irrigation", "equals", True, "Micro Irrigation Technical Guidelines", "verified", ...
# Notice True was expected_value, but mandatory True was missing before "Micro Irrigation Technical Guidelines"
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "Micro Irrigation Technical Guidelines"',
    '"irrigation.has_irrigation", "equals", True, True, "Micro Irrigation Technical Guidelines"'
)

# Check any other has_irrigation equals True
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "Polyhouse Technical Feasibility"',
    '"irrigation.has_irrigation", "equals", True, True, "Polyhouse Technical Feasibility"'
)
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "Nursery Feasibility"',
    '"irrigation.has_irrigation", "equals", True, True, "Nursery Feasibility"'
)
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "Mulberry Agronomy Norms"',
    '"irrigation.has_irrigation", "equals", True, True, "Mulberry Agronomy Norms"'
)
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "Orchard Plantation Norms"',
    '"irrigation.has_irrigation", "equals", True, True, "Orchard Plantation Norms"'
)
content = content.replace(
    '"irrigation.has_irrigation", "equals", True, "ESCOM Agricultural Consumer Norms"',
    '"irrigation.has_irrigation", "equals", True, True, "ESCOM Agricultural Consumer Norms"'
)

p.write_text(content, encoding="utf-8")
print("Fixed argument alignment for has_irrigation rules!")

