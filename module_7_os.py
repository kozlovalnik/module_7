import os
import time
from os.path import pardir

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.getcwd()
        fullpath = os.path.join(os.getcwd(), file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.pardir
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize}, Время изменения {formatted_time}, Родительская директория {parent_dir}')
    break