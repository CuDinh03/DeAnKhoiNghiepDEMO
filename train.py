from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="bottle-dataset/data.yaml",
    epochs=200,
    imgsz=640,
    batch=2,
    device="0",  
       workers=0,
    augment=True,
    patience=50
)
