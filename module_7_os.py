import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        fullpath = os.path.join(root, file)
        filetime = os.path.getmtime(fullpath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(fullpath)
        parent_dir = os.path.pardir
        print(f'Обнаружен файл: {file}, Путь: {root}, Размер: {filesize}, Время изменения {formatted_time}, Родительская директория {parent_dir}')
    break