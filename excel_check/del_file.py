# coding:utf-8
import os
import shutil


def remove_folder(path):
    shutil.rmtree(path)
    os.mkdir(path)

