from flask import Blueprint, current_app, jsonify, request
from werkzeug.utils import secure_filename
import os
import uuid

from core.image_processor import analyze_image
from core.material_analyzer import recommend_materials
from core.durability_predictor import predict_durability
from core.learning_engine import FeedbackStore
from api.utils import allowed_file

api = Blueprint("api", __name__)
feedback_store = FeedbackStore()


@api.get("/health")
def health():
    return jsonify({"status": "ok", "service": "adaptive-shoe-design"})


@api.post("/analyze-shoe")
def analyze_shoe():
    image = request.files.get("image")
    if image is None or not image.filename:
        return jsonify({"error": "An image field is required."}), 400
    if not allowed_file(image.filename, current_app.config["ALLOWED_EXTENSIONS"]):
        return jsonify({"error": "Unsupported image type."}), 415

    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
    filename = f"{uuid.uuid4().hex}_{secure_filename(image.filename)}"
    path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    image.save(path)

    visual = analyze_image(path)
    materials = recommend_materials(visual)
    durability = predict_durability(visual, materials)
    return jsonify({"image": filename, "visual_analysis": visual,
                    "materials": materials, "durability": durability})


@api.get("/materials")
def materials():
    return jsonify(recommend_materials({}))


@api.post("/feedback")
def feedback():
    payload = request.get_json(silent=True) or {}
    if not payload.get("rating"):
        return jsonify({"error": "rating is required"}), 400
    feedback_store.add(payload)
    return jsonify({"accepted": True, "samples": feedback_store.count()})
