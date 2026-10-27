from pathlib import Path
from ultralytics import YOLO

project_dir = Path(__file__).resolve().parent
model_path = project_dir / "models" / "license_plate_detector.pt"

print("Checking model file...")

if not model_path.exists():
    print("ERROR: Model file not found.")
else:
    print("Model file found.")
    print("Loading model...")

    try:
        model = YOLO(str(model_path))
        print("SUCCESS: Model loaded correctly.")
        print("Model task:", model.task)

    except Exception as error:
        print("ERROR: Model could not be loaded.")
        print(type(error).__name__, error)