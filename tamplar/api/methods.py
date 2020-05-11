import os
import shutil
import subprocess

import git

from tamplar.__internal import utils, init as init_pkg


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
    params = init_pkg.init_params()
    dst_path_ = os.path.abspath(f'{dst_path}') + '/'
    git.Git(dst_path_).clone(f'{init_pkg.account}/{init_pkg.repo_name}.git')
    init_pkg.init_package(params, src_path, dst_path)
    init_pkg.init_tmpl(params=params, path=dst_path)
    shutil.copyfile(os.path.expanduser('~') + params.pip_conf_path, src_path+'./deployments/.secrets/pip.conf') # TODO: not tested
    shutil.rmtree(src_path+'.git')
    init_pkg.init_readme(path=src_path)


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
