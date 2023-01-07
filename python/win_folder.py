# Создание папок в windows

import os

folder = "my_folder"
filename = os.path.join(r"f:\Лагерь", "Links", folder, "test.txt")
hd, tl = os.path.split(filename)
if not os.path.exists(hd):
    os.makedirs(hd)

with open(filename, "w") as f:
    f.write("123")
