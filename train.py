from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="bottle-dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=2,
    device="cpu",  #thay bằng GPU nếu máy có GPU
    augment=True,
    patience=50
)
