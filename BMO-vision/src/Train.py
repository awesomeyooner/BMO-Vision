from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data='C:/Users/aweso/Documents/BoeingVision/src/config.yaml', epochs=250, workers=0)