#!/usr/bin/python3

import os
from shutil import copyfile

files = os.listdir(os.getcwd())

for file in files:
    if os.path.isdir(file):
        copyfile(file, 'dragon')

print(os.getcwd())


