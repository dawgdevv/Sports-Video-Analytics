from ultralytics import YOLO

model = YOLO("model_1/last.pt")
model.predict("input_video.mp4", conf = 0.2 ,save = True)
