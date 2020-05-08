import os
import shutil


def clean(src):
    if os.path.exists(src):
        shutil.rmtree(f'{src}')
    os.mkdir(src)


def create(folders):
    for f in folders:
        if os.path.isdir(f):
            shutil.rmtree(f)
        os.mkdir(f)
