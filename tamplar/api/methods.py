import os
import shutil
import subprocess

from tamplar.__internal import utils, init as init_pkg

import git
from compose.cli import command as command_compose


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
    init_pkg.init_envs(params=params, path=dst_path)
    init_pkg.init_docker_compose(params=params, path=dst_path)
    shutil.copyfile(params.pip_conf_path, src_path+'./deployments/.secrets/pip.conf') # TODO: not tested
    shutil.rmtree(src_path+'.git')
    init_pkg.init_readme(path=src_path, params=params)
    init_pkg.init_gitignore(src_path=src_path)  # TODO: not tested


def kill(src_path=None):
    if src_path is None:
        src_path = './'
    paths = [f'{src_path}docker-compose.full.yml', f'{src_path}docker-compose.env.yml']
    project_dir = '.'
    for file_path in paths:
        project = command_compose.get_project(project_dir, [file_path])
        project.kill()


def run(src_path=None, mode='full'):  # TODO: not tested
    if src_path is None:
        src_path = './'
    if mode == 'full':
        file_path = f'{src_path}docker-compose.full.yml'
    elif mode == 'env':
        file_path = f'{src_path}docker-compose.env.yml'
    else:
        raise NotImplementedError('undefined mode')
    project_dir = '.'
    project = command_compose.get_project(project_dir, [file_path])
    services = project.up()
    failed = False
    codes = {}
    for s in services:
        codes[s.name] = s.exit_code
        if s.exit_code == 0:
            continue
        failed = True
    if not failed:
        print(f'all service exited with zero status codes. state: {list(codes.keys())}')
        return
    project.kill()
    print(f'all service exited with NON-zero status codes. state: {codes}')


def upload(src_path=None, pypi=True, docker=True):
    raise NotImplementedError()
    if src_path is None:
        src_path = './'
    file_path = f'{src_path}docker-compose.full.yml'
    project_dir = '.'
    project = command_compose.get_project(project_dir, [file_path])
    services = project.build()

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


def test(mode='integration', src_path=None):
    if src_path is None:
        src_path = './'
    if mode == 'integration':
        run(src_path=src_path, mode='full')
        pass
        kill(src_path=src_path)
    elif mode == 'unit':
        pass


def validate(src_path=None):
    raise NotImplementedError()
