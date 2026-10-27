
import cv2
from pathlib import Path

# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "images" / "parking.jpg"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# 2. LOAD IMAGE
# ==========================================

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(
        f"Cannot load image: {IMAGE_PATH}\n"
        "Check that the image is named parking.jpg."
    )

print("Parking image loaded successfully.")
print(f"Image dimensions: {image.shape[1]} x {image.shape[0]}")

# ==========================================
# 3. DEFINE PARKING SPACE COORDINATES
# Coordinates: (x, y, width, height)
# For the supplied 369 x 219 image.
# ==========================================

parking_spaces = [
    # Top row: 5 spaces
    (42, 29, 56, 79),    # Space 1
    (98, 29, 56, 79),    # Space 2
    (154, 29, 56, 79),   # Space 3
    (210, 29, 56, 79),   # Space 4
    (266, 29, 58, 79),   # Space 5

    # Bottom row: 3 spaces
    (42, 109, 56, 82),   # Space 6
    (98, 109, 56, 82),   # Space 7
    (154, 109, 56, 82),  # Space 8
]

# ==========================================
# 4. ANALYZE PARKING SPACES
# ==========================================

result = image.copy()

occupied_count = 0
available_count = 0

for index, (x, y, w, h) in enumerate(parking_spaces, start=1):

    roi = image[y:y + h, x:x + w]

    if roi.size == 0:
        continue

    # Convert the region to grayscale.
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Estimate occupancy from dark pixels.
    # This is a simple heuristic for the supplied illustration.
    dark_pixels = cv2.countNonZero(
        cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)[1]
    )

    dark_ratio = dark_pixels / (gray.shape[0] * gray.shape[1])

    # Initial threshold; visual calibration is required.
    is_occupied = dark_ratio > 0.18

    if is_occupied:
        color = (0, 0, 255)
        label = "OCCUPIED"
        occupied_count += 1
    else:
        color = (0, 255, 0)
        label = "AVAILABLE"
        available_count += 1

    # Draw parking-space boundaries.
    cv2.rectangle(
        result,
        (x, y),
        (x + w, y + h),
        color,
        2
    )

    # Display space number.
    cv2.putText(
        result,
        str(index),
        (x + 3, y + 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        color,
        1
    )

# ==========================================
# 5. DISPLAY SUMMARY
# ==========================================

summary = (
    f"Total: {len(parking_spaces)} | "
    f"Occupied: {occupied_count} | "
    f"Available: {available_count}"
)

cv2.rectangle(result, (0, 0), (result.shape[1], 22), (40, 40, 40), -1)

cv2.putText(
    result,
    summary,
    (5, 16),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.43,
    (255, 255, 255),
    1
)

# ==========================================
# 6. SAVE OUTPUT
# ==========================================

output_path = OUTPUT_DIR / "parking_result.jpg"

cv2.imwrite(str(output_path), result)

print("\n========== PARKING INSPECTION ==========")
print(f"Total spaces:     {len(parking_spaces)}")
print(f"Estimated occupied: {occupied_count}")
print(f"Estimated available: {available_count}")
print(f"Saved result: {output_path}")
print("========================================")

# ==========================================
# 7. DISPLAY RESULT
# ==========================================

cv2.imshow("Smart Parking Space Detection", result)

print("\nPress Q to close the window.")

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

