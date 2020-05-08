import os
import shutil
import subprocess

import git
from setuptools import sandbox as setuptools_

from tamplar.__internal import utils


repo_name = 'python-service-layout'
account = 'git://github.com/Hedgehogues'


def deps():
    """
    install dependencies from requirements
    :return:
    """
    print('install dependencies')
    subprocess.call(['pip', 'install', '-r', 'requirements'])


def init(agree=None, src_path=None, dst_path=None):
    """
    init is used to initialize new project

    :param agree: is need to clean
    :param src_path: path to repo of cloning
    :param dst_path: path to repo of extract
    :return:
    """
    if src_path is None:
        src_path = './'
    if dst_path is None:
        dst_path = './'
    print('initialize new service')
    cleaned = utils.clean_directory(path=src_path, agree=agree)
    if not cleaned:
        return
    prj_name = utils.input_('Please enter project name (available letters: digits, latin alphanum, -, _, space)')
    assert len(prj_name) > 0, 'project name must be not empty'
    utils.name_validator(prj_name)
    src_path_ = os.path.abspath(f'{src_path}{repo_name}/')
    dst_path_ = os.path.abspath(f'{dst_path}') + '/'
    git.Git(dst_path_).clone(f'{account}/{repo_name}.git')
    utils.mv(src=src_path_, dst=dst_path_)
    pkg_name = utils.package_name(prj_name)
    pkg_src_path = f'{src_path}{repo_name.replace("-", "_")}/'
    pkg_dst_path = f'{dst_path_}{pkg_name}/'
    utils.mv(src=pkg_src_path, dst=pkg_dst_path)
    os.rename(f'{dst_path_}setup.tmpl', f'{dst_path_}setup.py')
    os.rename(f'{dst_path_}info.tmpl', f'{dst_path_}info.py')
    with open(f'{dst_path_}info.py') as fd:
        lines = fd.read()
    with open(f'{dst_path_}info.py', 'w') as fd:
        lines = lines.replace(repo_name, prj_name)
        fd.write(lines)


def run(mode='local', daemon=None):
    raise NotImplementedError()
    # full
    # env
    # compose.TopLevelCommand()


def upload(pypi=None, docker=None):
    raise NotImplementedError()
    # args = ['bdist_wheel', 'upload']
    # if pypi is not None:
    #     args += ['-r', pypi]
    # setuptools_.run_setup('setup.py', pypi)
    # if docker is None:
    #     return
    # docker
    # pypi


def clean(src_path=None):
    """
    This method is used to clean repo from built files

    :param src_path: path to repo of cleaning
    :return:
    """
    if src_path is None:
        src_path = './'
    folders = ['build', 'dist']
    for f in folders:
        if not os.path.isdir(f'{src_path}/{f}'):
            continue
        shutil.rmtree(f'{src_path}/{f}')
    for name in os.listdir(path=src_path):
        suffix = name[-len('.egg-info'):]
        if suffix != '.egg-info':
            continue
        if not os.path.isdir(f'{src_path}/{name}'):
            continue
        shutil.rmtree(f'{src_path}/{name}')


def test(mode):
    raise NotImplementedError()
