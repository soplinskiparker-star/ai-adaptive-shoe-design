# AI Adaptive Shoe Design

Editable Flask starter for image-assisted shoe concept analysis. It accepts an uploaded image, records basic visual measurements, returns candidate materials, and stores explicit user feedback for later model training.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Upload an image:

```bash
curl -F image=@shoe.jpg http://localhost:5000/api/analyze-shoe
```

## Important limitations

The starter does **not** infer material identity, safety, or an eight-month lifespan from a photograph. Those claims require labeled data and physical testing. “LightSpray,” PHA processing, bacteria-based cooling, and other biofabrication ideas must be treated as research concepts until validated by qualified materials, footwear, and biosafety professionals. Do not use live bacteria or wear prototypes without appropriate containment, testing, and safety review.

Feedback is stored locally in `data/user_feedback.json`; it is a dataset for future review, not autonomous self-modification. Add a reviewed training pipeline before retraining any model.
