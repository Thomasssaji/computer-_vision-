
from pathlib import Path
from ultralytics import YOLO

MODEL_PATH = Path("runs/detect/runs/traffic_sign/training/weights/best.pt")
TEST_DIR = Path("test_images")
OUTPUT_DIR = "final_test_results"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not TEST_DIR.exists():
    raise FileNotFoundError(f"Test folder not found: {TEST_DIR}")

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

images = sorted(
    p for p in TEST_DIR.iterdir()
    if p.is_file() and p.suffix.lower() in image_extensions
)

if not images:
    raise FileNotFoundError("No test images found.")

model = YOLO(str(MODEL_PATH))

print("\n========== TRAFFIC SIGN RECOGNITION ==========")
print("Model classes:", model.names)
print("Images to test:", len(images))

for image_path in images:
    print(f"\nImage: {image_path.name}")

    results = model.predict(
        source=str(image_path),
        conf=0.25,
        iou=0.45,
        imgsz=640,
        save=True,
        project=OUTPUT_DIR,
        name="predictions",
        exist_ok=True,
        verbose=False
    )

    for result in results:
        if result.boxes is None or len(result.boxes) == 0:
            print("  No detections.")
            continue

        for box in result.boxes:
            class_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            class_name = result.names[class_id]

            coords = [
                round(float(v), 1)
                for v in box.xyxy[0].tolist()
            ]

            print(f"  Class: {class_name}")
            print(f"  Confidence: {confidence:.2%}")
            print(f"  Bounding box: {coords}")

print("\n========== TESTING COMPLETE ==========")
print(f"Annotated images: {OUTPUT_DIR}/predictions")

