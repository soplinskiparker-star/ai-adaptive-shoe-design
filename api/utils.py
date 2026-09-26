import json
import os
from typing import Any


def load_json(path: str, default: Any):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def allowed_file(filename: str, allowed_extensions: set[str]) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions
