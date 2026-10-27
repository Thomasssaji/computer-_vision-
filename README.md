# Traffic Sign Detection and Recognition Using YOLO

## Project Overview

This project uses the YOLO object-detection framework to detect and classify traffic signs in images. It identifies four classes: crosswalk, speed limit, stop, and traffic light.

## Technologies Used

* Python
* Ultralytics YOLO
* OpenCV
* PyTorch
* Pascal VOC XML annotations
* YOLO dataset format

## Dataset

The dataset contains 877 images with corresponding XML annotations. The annotations were converted into YOLO format and split into training and validation sets.

* Training images: 701
* Validation images: 176
* Classes: 4

## Model Performance

The trained model achieved the following validation results:

| Metric    |  Score |
| --------- | -----: |
| mAP@50    | 90.93% |
| mAP@50–95 | 77.12% |
| Precision | 92.26% |
| Recall    | 88.89% |

These metrics represent performance on the validation dataset.

## Features

* Detects traffic signs in images.
* Predicts the traffic-sign class.
* Reports confidence scores and bounding-box coordinates.
* Saves annotated prediction images.
* Evaluates model performance on a validation dataset.

## Supported Classes

1. Crosswalk
2. Speed limit
3. Stop
4. Traffic light

The model is not designed to recognize traffic-sign classes outside these four categories.

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Evaluate the trained model:

```bash
python evaluate_model.py
```

Test images:

```bash
python test_model.py
```

## Project Limitations

Detection performance can vary with lighting, image quality, sign size, viewing angle, and background conditions. Further testing on diverse unseen images is required to assess generalization.

## Future Improvements

* Expand the dataset with additional traffic-sign categories.
* Improve detection in challenging lighting and weather conditions.
* Evaluate performance on a larger independent test set.
* Explore real-time detection using a camera.

## Author

Add your name, department, institution, and project details here.
