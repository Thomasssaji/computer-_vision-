# Vehicle License Plate Detection and Recognition

## Overview

This project implements a computer vision system for detecting vehicle license plates in images and extracting the plate text using Optical Character Recognition (OCR).

The system uses a trained YOLO model to detect license plate regions and an OCR component to recognize the characters within the detected plates.

## Features

* Detects license plates in vehicle images.
* Uses a trained deep learning model.
* Extracts license plate regions for text recognition.
* Displays detection confidence and bounding box coordinates.
* Saves or displays detection results.

## Technologies Used

* Python
* YOLO
* PyTorch
* OpenCV
* Optical Character Recognition (OCR)

## Project Structure

```text
Vehicle_License_Plate_Recognition/
├── models/
│   └── best.pt
├── images/
│   └── car1.jpg
├── detect_plate.py
├── requirements.txt
├── README.md
└── .gitignore
```

Additional Python modules should be included if the implementation depends on them.

## Installation

Install Python and clone or download this repository.

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Place a test vehicle image in the images folder.

Run:

```bash
python detect_plate.py
```

Follow any image-path instructions defined in the program.

## Model

The trained model is stored in `models/best.pt`.

## Limitations

Recognition performance depends on image quality, lighting, viewing angle, plate visibility, and the accuracy of the trained model.

## Future Improvements

* Improve OCR accuracy.
* Support video and live camera input.
* Handle multiple vehicles in a single image.
* Improve performance under poor lighting and angled views.
* Add a graphical user interface.

## Disclaimer

This project is intended for educational and research purposes. Use vehicle images and license plate information responsibly and comply with applicable privacy requirements.
