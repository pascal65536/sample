# Разложить картинки по папкам, папка - дата создания файла

import os
import shutil
import platform
import datetime
from PIL import Image, ExifTags, UnidentifiedImageError



def creation_date(path_to_file):
    """
    http://stackoverflow.com/a/39501288/1709587
    https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image
    """
    if platform.system() == 'Windows':
        ret = datetime.datetime.fromtimestamp(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            ret = datetime.datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            ret = datetime.datetime.fromtimestamp(stat.st_mtime)

    img_exif = None
    if path_to_file[-3:] in ['JPG', 'jpg', 'png']:
        try:
            img = Image.open(path_to_file)
            img_exif = img.getexif()
        except (FileNotFoundError, UnidentifiedImageError):
            pass
            # os.remove(path_to_file)

    if img_exif is not None:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                if ExifTags.TAGS[key] in ['DateTime']:
                    ret = datetime.datetime.strptime(val, '%Y:%m:%d %H:%M:%S')
    return ret


if __name__ == '__main__':
    new_filepath = '/home/pascal65536/Загрузки/000/'
    filepath = '/home/pascal65536/Загрузки/'
    for address, dirs, files in os.walk(filepath):
        for f in files:
            print(f)
            if 'мир' in f:
                continue
            src = os.path.join(address, f)
            dd = creation_date(src)
            fldr_name = f'{dd}'[:10]
            fldr = os.path.join(new_filepath, fldr_name)
            os.makedirs(fldr, exist_ok=True)
            dst = os.path.join(fldr, f)
            shutil.copy2(src, dst)
            os.remove(src)
