from PIL import Image
import os

folder = "bottle-dataset/train/images"

for f in os.listdir(folder):
    path = os.path.join(folder, f)
    try:
        img = Image.open(path)
        img.verify()  # kiểm tra xem ảnh có bị hỏng không
    except Exception as e:
        print("Corrupt:", f)
