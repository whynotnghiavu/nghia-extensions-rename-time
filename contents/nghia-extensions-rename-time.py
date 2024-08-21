import os
from time import sleep
from datetime import datetime
# pip install tqdm
from tqdm import tqdm


folder_path = r"input-nghia-rename-time"
folder_path = r"/home/vvn20206205/Desktop/input-nghia-rename-time"
folder_path = r"/home/vvn20206205/Desktop/input"
folder_path = r"C:\Users\vvn20206205\Desktop\metHe"


if not os.path.exists(folder_path):
    print(f"Không có thư mục {folder_path}")
    os.mkdir(folder_path)


for count, filename in enumerate(tqdm(os.listdir(folder_path))):
    # for count, filename in enumerate(os.listdir(folder_path)):

    now = datetime.now()
    now = now.strftime("%Y%m%d%H%M%S%f")
    # print(f"🚀 {now}")

    full_path = os.path.join(folder_path, filename)
    name, ext = os.path.splitext(filename)
    new_name = f"{name}{now}{ext}"

    os.rename(full_path, os.path.join(folder_path, new_name))
    sleep(0.5)
