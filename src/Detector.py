from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.model = YOLO('weights/yolov8m.pt')

    def find_people(self, frame):
        results = self.model(frame, classes=[0], conf=0.5)[0]
        return results.boxes.xyxy.numpy().tolist()