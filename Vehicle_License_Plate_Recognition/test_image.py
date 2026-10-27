import cv2
from pathlib import Path

# Get the project folder
project_folder = Path(__file__).resolve().parent

# Get the image path
image_path = project_folder / "images" / "car1.jpg"

# Check whether the image exists
if not image_path.exists():
    print("ERROR: Image file not found!")
    print("Expected location:", image_path)

else:
    # Load the image
    image = cv2.imread(str(image_path))

    if image is None:
        print("ERROR: OpenCV could not read the image.")

    else:
        height, width, channels = image.shape

        print("SUCCESS: Image loaded correctly!")
        print("Image location:", image_path)
        print("Image width:", width)
        print("Image height:", height)
        print("Image channels:", channels)
        print("Image test completed successfully!")