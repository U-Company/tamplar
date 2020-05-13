import os
import shutil


input_ = input

tamplar_config = '.tamplar'


def mv(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.abspath(os.path.join(src, item))
        d = os.path.abspath(os.path.join(dst, item))
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
    shutil.rmtree(src)


def empty_folder(objs):
    empty = len(objs) == 0
    idea = len(objs) == 1 and objs[0] == '.idea'
    return empty or idea


def clean_directory(path, agree=None):
    if agree is not None:
        agree = agree.lower()
    assert agree in ['y', 'n', None], "agree must be  ['y', 'n', None']"
    objs = os.listdir(path=path)
    if empty_folder(objs):
        return True
    clean = agree
    if agree is None:
        clean = input_('directory is not empty. All files will be remove [Y/n]: ')
    clean = clean.lower()
    assert clean in ['y', 'n', '']
    if clean == 'n':
        return False
    for obj in objs:
        if os.path.isdir(path+obj):
            shutil.rmtree(path+obj)
            continue
        os.remove(path+obj)
    return True
