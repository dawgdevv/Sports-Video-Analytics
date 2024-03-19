# Problem statement(A4) for HackJKLU 3.0

## Data Source

- Data Source: Roboflow.com
- Data Name: "Tennis Ball Detection Image Dataset"
- Dataset-1 Link: [https://universe.roboflow.com/viren-dhanwani/tennis-ball-detection/dataset/6](https://universe.roboflow.com/viren-dhanwani/tennis-ball-detection/dataset/6)
- Dataset-2 Link: [https://drive.google.com/file/d/1lhAaeQCmk2y440PmagA0KmIVBIysVMwu/view?usp=drive_link](https://drive.google.com/file/d/1lhAaeQCmk2y440PmagA0KmIVBIysVMwu/view?usp=drive_link)

## Processing

- Convert videos to a suitable format for analysis (frames).

## Ball Tracking

- Object Detection: Utilize object detection YOLOv8 (You Only Look Once). These algorithms excel at real-time object detection. Trained the model on a dataset of tennis balls in various lighting conditions and backgrounds.
- Models Trained:
  -Ball Detection Model (Trained on Custom Dataset)
  -Player Identification Model (Pre-Trained)
  -Court Detection Model (Trained on Custom Dataset)

## Contributors
- Nishant Raj
- Dev Rishi Verma
- Dhruv Sharma
- Rajyavardhan Singh
- Riyansh Verma