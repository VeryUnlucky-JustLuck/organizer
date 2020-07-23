#!/usr/bin/python3

import os

path = os.getcwd()
pathlist = os.listdir(path)
user_true = input("1:rename, 2:remove_name")
user_rename = input("Insert rename:")
if (user_true == "1"):
    for file in pathlist:
        os.rename(file, (user_rename + file))
elif (user_true == "2"):
    for file in pathlist:
        os.rename(file, file.replace(user_rename, ""))
