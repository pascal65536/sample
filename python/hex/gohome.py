# Разложить картинки по папкам, папка - дата создания файла

import os
import shutil
import platform
import datetime
from PIL import Image, ExifTags


def walk(fp):
    ret = list()
    # import ipdb; ipdb.set_trace()
    for address, dirs, files in os.walk(fp):
        for dir in dirs:
            if dir[0] == ".":
                continue
            fp = os.path.join(address, dir)
            ret.append(fp)
    return ret


if __name__ == "__main__":
    filepath = "/media/pascal65536/021F03A515315EB5/Фотокамера"
    filepath_src = "/media/pascal65536/021F03A515315EB5/Фотокамера/Фотокамера"
    filepath_lst = walk(filepath_src)
    for fp in filepath_lst:
        for address, dirs, files in os.walk(fp):
            if dirs:
                continue
            for f in files:
                src = os.path.join(address, f)
                dst = os.path.join(filepath, f)
                shutil.copy2(src, dst)
                os.remove(src)
                # import ipdb; ipdb.set_trace()

    #             # if 'мир' in f:
    #             #     continue
    #             # src = os.path.join(address, f)
    #             # dd = creation_date(src)
    #             # fldr_name = f'{dd}'[:10]
    #             # fldr = os.path.join(address, fldr_name)
    #             # os.makedirs(fldr, exist_ok=True)
    #             # dst = os.path.join(fldr, f)

    # print('-' * 80)
