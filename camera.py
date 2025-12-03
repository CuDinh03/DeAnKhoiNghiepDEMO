from ultralytics import YOLO
import cv2

# Load model đã train
model = YOLO("runs/detect/train/weights/best.pt")

# Class mapping theo data.yaml
class_names = {0: "cup", 1: "bottle"}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Không mở được camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Predict frame
    results = model.predict(frame, conf=0.3, imgsz=480)

    # Annotate frame
    annotated_frame = results[0].plot()

    # Đếm số lượng từng class
    counts = {name: 0 for name in class_names.values()}
    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls)
            if cls_id in class_names:
                counts[class_names[cls_id]] += 1

    # Hiển thị số lượng lên frame
    y0 = 40
    for i, (name, count) in enumerate(counts.items()):
        cv2.putText(annotated_frame, f"{name}: {count}", (20, y0 + i*40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Bottle & Cup Detection", annotated_frame)

    # Nhấn ESC để thoát

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
