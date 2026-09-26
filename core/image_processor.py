"""Lightweight, replaceable image-analysis adapter.

This deliberately returns measurable observations rather than pretending to identify
materials from pixels. Replace this adapter with a validated vision model later.
"""
from PIL import Image
import numpy as np


def analyze_image(path: str) -> dict:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        pixels = np.asarray(rgb, dtype=np.float32)
    brightness = float(pixels.mean() / 255.0)
    contrast = float(pixels.std() / 255.0)
    return {
        "width": int(pixels.shape[1]), "height": int(pixels.shape[0]),
        "brightness": round(brightness, 3), "contrast": round(contrast, 3),
        "material_identification": "requires laboratory or trained vision model"
    }
