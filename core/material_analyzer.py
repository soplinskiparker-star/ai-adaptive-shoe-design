from typing import Any

MATERIALS = [
    {"name": "PHA-based polymer", "use": "experimental upper or flexible part", "notes": "Verify biocompatibility, moisture resistance, and abrasion performance."},
    {"name": "TPU", "use": "sole lattice and flexible zones", "notes": "Common additive-manufacturing candidate; validate fatigue and slip resistance."},
    {"name": "Bio-based foam", "use": "cushioning", "notes": "Measure compression set, sweat exposure, and hydrolysis before use."},
    {"name": "LightSpray-inspired coating", "use": "lightweight sprayed surface concept", "notes": "This is a concept reference, not a guaranteed process or material."}
]


def recommend_materials(observations: dict[str, Any]) -> list[dict[str, str]]:
    return MATERIALS
