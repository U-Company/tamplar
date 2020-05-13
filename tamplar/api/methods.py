import os
import shutil
import subprocess

from compose import service

from tamplar.__internal import utils, init as init_pkg

import git
from compose.cli import command as command_compose


codes = {}


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
    init_pkg.init_templates(params=params, path=dst_path)
    shutil.copyfile(params.pip_conf_path, src_path+'./deployments/.secrets/pip.conf')
    shutil.rmtree(src_path+'.git')
    init_pkg.init_readme(path=src_path, params=params)
    init_pkg.init_gitignore(src_path=src_path)


def kill(src_path=None):
    """
    kill is used to kill your docker-compose (like docker-compose kill)
    :param src_path: path to folder of killing docker-compose
    :return:
    """
    if src_path is None:
        src_path = './'
    path = src_path + 'deployments/'
    paths = [f'{path}docker-compose.full.yml', f'{path}docker-compose.env.yml']
    project_dir = '.'
    for file_path in paths:
        project = command_compose.get_project(project_dir, [file_path])
        project.kill()


def run(src_path=None, mode='full', build='yes'):
    """
    run is used to run (like docker-compose up)
    :param src_path: path to folder of running package
    :param mode:
        full or env:
            - env is environment running.
            - full is service with environment running
    :param build: is needed to build service container (like docker-compose up --build)
    :return:
    """
    global codes
    if src_path is None:
        src_path = './'
    if mode == 'full':  # TODO: NOT TESTED
        file_path = f'{src_path}deployments/docker-compose.full.yml'
    elif mode == 'env':
        file_path = f'{src_path}deployments/docker-compose.env.yml'
    else:
        raise NotImplementedError('undefined mode')
    if mode == 'full':
        print('building container')
    project = command_compose.get_project(project_dir='.', config_path=[file_path])
    build = build.lower()
    if build == 'yes':
        build_mode = service.BuildAction.force
    elif build == 'no':
        build_mode = None
    else:
        raise NotImplementedError('build may be only [yes, no]')
    services = project.up(detached=True, do_build=build_mode)
    if mode == 'full':
        print('container started')
    failed = False
    codes = {}
    for s in services:
        if s.exit_code == 137:
            codes[s.name] = init_pkg.DockerCompose.Started
            continue
        if s.exit_code == 0:
            codes[s.name] = init_pkg.DockerCompose.AlreadyWorks
            continue
        codes[s.name] = f'status code: {s.exit_code}'
        failed = True
    if not failed:
        print(f'OK. all service exited with zero status codes. services: {codes}')
        return
    project.kill()  # TODO: NOT TESTED
    print(f'FAILED. all service exited with NON-zero status codes. state: {codes}')
    return


def upload(src_path=None, pypi='yes', docker=True):
    """
    NOT IMPLEMENTED

    upload is used to upload package to docker registry and pypi registry
    :param src_path: path to folder of uploading package
    :param pypi: yes or no is needed to upload your package into pypi registry
    :param docker: yes or no is needed to upload your package into docker registry
    :return:
    """
    raise NotImplementedError()
    if src_path is None:
        src_path = './'
    file_path = f'{src_path}deployments/docker-compose.full.yml'
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
    clean is used to clean repo from built files
    :param src_path: path to folder of cleaning
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
    """
    NOT IMPLEMENTED

    test is used to test your project
    :param mode: integration or unit
    :param src_path: path to folder of testing
    :return:
    """
    raise NotImplementedError()
    if src_path is None:
        src_path = './'
    if mode == 'integration':
        run(src_path=src_path, mode='full')
        pass
        kill(src_path=src_path)
    elif mode == 'unit':
        pass


def validate(src_path=None):
    """
    NOT IMPLEMENTED

    validate is used to validate your project with https://github.com/U-Company/python-service-layout by rules
    :param src_path: path to folder of validation
    :return:
    """
    raise NotImplementedError()
