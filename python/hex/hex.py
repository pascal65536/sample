# Найти дубликаты файлов в указанной папке.
# Обойти папку рекурсивно. Для каждого найденого файла найти hash-сумму.
# Сгруппировать файлы по hash-суммам.
# Если для одной и той же hash-суммы нашлось несколько файлов, то они считаются дубликатами.
# https://python-scripts.com/md5-sha1

import hashlib
import os


def get_digest(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as file:
        fl = file.read()
        h.update(fl)
    return h.hexdigest()


if __name__ == "__main__":
    hex_file_dct = dict()
    filepath = "/media/pascal65536/021F03A515315EB5/Фотокамера/"
    for address, dirs, files in os.walk(filepath):

        for name in files:
            filename = os.path.join(address, name)
            ret = get_digest(filename)
            hex_file_dct.setdefault(ret, list())
            hex_file_dct[ret].append(filename)

    count = 0
    for has, file_list in hex_file_dct.items():
        for filename in file_list[1:]:
            print(filename)
            os.remove(filename)
            count += 1
    print(f"Удалено файлов: {count}")
