# 🧠 Bottle & Cup Detection AI (YOLOv8 + Camera)

Dự án này sử dụng **YOLOv8** để huấn luyện và nhận diện **chai (bottle)** và **cốc (cup)** trực tiếp từ **camera hoặc ảnh/video** trên cả **macOS và Windows**.

---

# I. CÔNG CỤ & PHẦN MỀM CẦN CHUẨN BỊ

## 1. Phần mềm bắt buộc (cả macOS & Windows)

| Phần mềm          | Mục đích                 |
| ----------------- | ------------------------ |
| Python 3.9 – 3.11 | Chạy YOLO, xử lý ảnh     |
| Git               | Clone project từ GitHub  |
| VS Code / PyCharm | Viết & chạy code         |
| Camera / Webcam   | Nhận diện thời gian thực |

---

## 2. Cài đặt trên **macOS**

### ✅ Cài Python

Vào:
[https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)

Tải **Python 3.9.13

Sau khi cài, kiểm tra:

```bash
python3 --version
pip3 --version
```

### ✅ Cài Git

macOS thường có sẵn Git. Nếu chưa:

```bash
brew install git
```

Kiểm tra:

```
git --version
```

---

## 3. Cài đặt trên **Windows**

### ✅ Cài Python

Tải tại:
[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

⚠ Khi cài nhớ **tick vào**:
☑ Add Python to PATH

Kiểm tra:

```cmd
python --version
pip --version
```

### ✅ Cài Git for Windows

Tải tại:
[https://git-scm.com/download/win](https://git-scm.com/download/win)

Dùng Git Bash hoặc Command Prompt đều được.

---

# II. CLONE DỰ ÁN TỪ GITHUB

Mở Terminal (macOS) hoặc Git Bash / CMD (Windows):

```
git clone https://github.com/CuDinh03/DeAnKhoiNghiepDEMO.git
```
---

# III. TẠO MÔI TRƯỜNG ẢO (VENV)

## macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Nếu thành công, bạn sẽ thấy:

```
(.venv)
```

---

# IV. CÀI THƯ VIỆN CẦN THIẾT

Chạy lệnh:

```bash
pip install --upgrade pip
pip install ultralytics opencv-python pillow matplotlib labelImg
```

Kiểm tra YOLO:

```bash
yolo version
```

---

# V. CẤU TRÚC THƯ MỤC DATASET

Cấu trúc chuẩn:

```
bottle-dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

File `data.yaml`:

```yaml
train: train/images
val: valid/images

names:
  0: bottle
  1: cup
```

---

# VI. GÁN NHÃN ẢNH (LABEL)

Mở tool:

```bash
labelImg
```

Thiết lập:

* Format: **YOLO**
* Classes:

  * bottle
  * cup

Sau đó vẽ khung quanh chai và cốc trong ảnh.

---

# VII. TRAIN MODEL YOLOV8 

Lưu ý vào file train.py thay đổi CPU thành GPU nếu máy có GPU 

Chạy:

``` bash
pyhton3 train.py
```

Sau khi train, model sẽ nằm tại:

```
runs/detect/train/weights/best.pt
```

✅ Đây là file AI đã học xong.

---

# VIII. NHẬN DIỆN BẰNG CAMERA (REALTIME)

Chạy:

```bash
python camera.py
```

---

# IX. LỖI THƯỜNG GẶP & CÁCH SỬA

## 1. Không có `best.pt`

Kiểm tra:

```
runs/detect/train*/weights/
```

Đảm bảo train thành công.

---

## 2. Camera không mở được

### macOS:

Vào:
System Settings → Privacy & Security → Camera
Cho phép Terminal/Python

### Windows:

Cho phép camera cho app Desktop trong:
Privacy Settings → Camera

---

# X. CÔNG NGHỆ SỬ DỤNG

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* LabelImg
* macOS / Windows
* AI Object Detection

---

🚀 Dự án có thể mở rộng thành:

* Nhận diện nhiều vật thể hơn
* Xuất excel số lượng
* Làm website Flask / Django
* Kết nối IoT camera
