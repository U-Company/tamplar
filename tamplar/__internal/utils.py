import os
import shutil
import string


input_ = input


def mv(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
    shutil.rmtree(src)


def name_validator(project_name):
    name_symbols = set(project_name.lower())
    all_symbols = string.ascii_lowercase + string.digits + ' -_'
    intersection = name_symbols.difference(all_symbols)
    assert len(intersection) == 0, 'invalid project name'


def package_name(name):
    return name.replace('-', '_').replace(' ', '_')


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
        clean = input_("Directory is not empty. All files will be remove [Y/n]:")
    clean = clean.lower()
    assert clean in ['y', 'n', '']
    if clean == 'n':
        return False
    for obj in objs:
        shutil.rmtree(path+obj)
    return True
