# from PIL import Image
# import os

# folder = "bottle-dataset/train/images"

# for f in os.listdir(folder):
#     path = os.path.join(folder, f)
#     try:
#         img = Image.open(path)
#         img.verify()  # kiểm tra xem ảnh có bị hỏng không
#     except Exception as e:
#         print("Corrupt:", f)


import torch

print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))

