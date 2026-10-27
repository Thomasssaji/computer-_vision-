from pathlib import Path
import cv2
from ultralytics import YOLO

# Project paths
project_dir = Path(__file__).resolve().parent
model_path = project_dir / "models" / "license_plate_detector.pt"
image_path = project_dir / "images" / "car1.jpg"
output_path = project_dir / "images" / "car1_detected.jpg"

print("Loading license plate detection model...")

model = YOLO(str(model_path))

print("Loading vehicle image...")

image = cv2.imread(str(image_path))

if image is None:
    print("ERROR: Could not load the input image.")
    raise SystemExit(1)

print("Running license plate detection...")

results = model.predict(
    source=image,
    conf=0.25,
    save=False,
    verbose=False
)

result = results[0]
detected_image = result.plot()

if result.boxes is not None and len(result.boxes) > 0:
    print("License plate detection completed.")
    print("Number of detected objects:", len(result.boxes))

    for i, box in enumerate(result.boxes, start=1):
        confidence = float(box.conf[0])
        coordinates = box.xyxy[0].tolist()

        print(f"Detection {i}:")
        print(f"Confidence: {confidence:.2f}")
        print(f"Coordinates: {coordinates}")
else:
    print("No license plates detected.")
    print("The image may not contain a clearly visible plate.")

cv2.imwrite(str(output_path), detected_image)

print("Output image saved to:")
print(output_path)

print("Opening the detected image...")

import os
os.startfile(str(output_path))