#!/usr/bin/python3

import os
import shutil

path = os.getcwd()
pathlist = os.listdir(path)
list = []

def check_extension():
    for file in pathlist:
        if os.path.splitext(file)[1] != '':
            list.append(os.path.splitext(file)[1])

def make_folder():
    for extension in set(list):
        if not os.path.isdir(extension):
            os.mkdir(extension)

def move_files():
    for file in pathlist:
        if os.path.exists(os.path.splitext(file)[1]):
            shutil.move(file, os.path.splitext(file)[1])

check_extension()
make_folder()
move_files()


