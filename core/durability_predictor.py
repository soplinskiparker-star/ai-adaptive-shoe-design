from typing import Any


def predict_durability(observations: dict[str, Any], materials: list[dict[str, str]],
                       target_months: int = 8) -> dict[str, Any]:
    return {
        "target_months": target_months,
        "estimated_months": None,
        "confidence": 0.0,
        "status": "prototype_only",
        "validation_required": [
            "mechanical flex-cycle testing", "abrasion testing", "wet/dry aging",
            "UV and temperature exposure", "slip and fit testing", "wearer safety review"
        ],
        "ways_to_extend_life": [
            "use replaceable high-wear components", "seal moisture-sensitive interfaces",
            "increase radii at stress concentrations", "inspect after every test cycle"
        ]
    }
