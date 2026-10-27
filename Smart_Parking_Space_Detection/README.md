# Smart Parking Space Detection

## Overview

Smart Parking Space Detection is a computer vision project developed using Python and OpenCV. It analyzes a parking lot image and estimates which parking spaces are occupied and which are available.

## Features

* Loads a parking lot image.
* Defines individual parking spaces using image coordinates.
* Estimates parking occupancy using image-processing techniques.
* Marks occupied spaces in red and available spaces in green.
* Displays the total number of spaces, occupied spaces, and available spaces.
* Saves the processed image to the output folder.

## Technologies Used

* Python
* OpenCV
* NumPy

## Project Structure

```text
Smart_Parking_Space_Detection/
├── images/
│   └── parking.jpg
├── output/
│   └── parking_result.jpg
├── parking_detection.py
├── requirements.txt
└── README.md
```

## Installation

Install Python, then install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command from the project directory:

```bash
python parking_detection.py
```

Press `Q` to close the output window.

## Methodology

The system uses manually defined parking-space coordinates and image processing to estimate occupancy. The current implementation is a prototype and may require coordinate and threshold calibration for other parking images.

## Future Improvements

* Automatically detect parking-space boundaries.
* Improve occupancy classification.
* Support live camera feeds.
* Develop a graphical user interface.
