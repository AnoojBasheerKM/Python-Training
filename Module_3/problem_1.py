import os
from importlib.metadata import files


def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)


path = 'C:\\Users\\anooj\\Desktop\\Python Training'

list_files(path)