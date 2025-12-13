from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train4/weights/best.pt")

class_names = {0: "cup", 1: "bottle"}

cap = cv2.VideoCapture("http://192.168.1.12:81/stream")

if not cap.isOpened():
    print("❌ Không mở được camera")
    exit()

cv2.namedWindow("ESP32-CAM Detection", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Mất stream, đang chờ reconnect...")
        continue

    results = model.predict(frame, conf=0.3, imgsz=480)
    annotated_frame = results[0].plot()

    counts = {name: 0 for name in class_names.values()}
    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls)
            if cls_id in class_names:
                counts[class_names[cls_id]] += 1

    y0 = 40
    for i, (name, count) in enumerate(counts.items()):
        cv2.putText(annotated_frame, f"{name}: {count}", (20, y0 + i*40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("ESP32-CAM Detection", annotated_frame)

    # Bắt ESC hoặc Q
    key = cv2.waitKey(10)
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
