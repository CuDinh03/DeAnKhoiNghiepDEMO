from PIL import Image
import os

folders = ["bottle-dataset/train/images", "bottle-dataset/valid/images"]

for folder in folders:
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        try:
            img = Image.open(path)
            img = img.convert("RGB")
            img.save(path)  # ghi đè, đảm bảo định dạng chuẩn
        except:
            print("Skipping corrupt file:", f)
