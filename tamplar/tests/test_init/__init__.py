import os

from tamplar import tests
from tamplar.api import methods
from tamplar.tests import utils
from tamplar.__internal import utils as _internal_utils


def assert_empty(folder, not_=False):
    if not_:
        assert len(os.listdir(folder)) != 0
        return
    assert len(os.listdir(folder)) == 0


def assert_exist_folder(folder, not_=False):
    if not_:
        assert not os.path.exists(folder)
        return
    assert os.path.exists(folder)
    assert os.path.isdir(folder)


def assert_info(folder, validates):
    with open(f'{folder}info.py') as fd:
        lines = fd.read().split('\n')
        values = dict([l.split(' = ') for l in lines])
        for k in values:
            values[k] = values[k][1:-1]
            found = k in validates
            checked = found and validates[k] == values[k]
            assert checked or not found
        print(values)


def assert_count_folders(folder, count_):
    assert len(os.listdir(folder)) == count_


def assert_validate_layout(folder, prj_name, additional=None):
    if additional is None:
        additional = []
    files = ['setup.py', 'info.py', 'requirements', 'README.md', 'makefile', '.gitignore', 'tests', 'service',
             'scripts', prj_name, 'logs', 'docs', 'deployments', 'data', 'configs'] + additional
    assert sorted(files) == sorted(os.listdir(folder))


def assert_service_name(folder, prj_name):
    with open(folder+'info.py', 'r') as fd:
        assert fd.read().find(prj_name) >= 0


def assert_pip_conf(folder, pip_conf_path):
    with open(pip_conf_path) as fd:
        pip_conf = fd.read()
    with open(folder+'deployments/.secrets/pip.conf', 'r') as fd:
        assert fd.read() == pip_conf


def assert_docker_compose_full(folder):
    with open(folder+'deployments/docker-compose.full.yml', 'r') as fd:
        assert fd.read().find('{{prj_name}}') == -1


def assert_envs(folder):
    with open(folder+'deployments/.envs/local.env', 'r') as fd:
        assert fd.read().find('{{PRJ_NAME}}') == -1


def assert_gitignore_tamplar(folder):
    with open(folder+'.gitignore', 'r') as fd:
        assert fd.read().find('.tamplar') != -1


class Core:
    def __init__(self, prj_name, author_name='', author_email='', description='', pip_conf=''):
        self.__count = -1
        self.prj_name = prj_name
        self.author_name = author_name
        self.author_email = author_email
        self.description = description
        self.pip_conf = pip_conf

    def __answer_is_not_none(self):
        if self.__count == 1:
            return self.prj_name
        elif self.__count == 2:
            return self.author_name
        elif self.__count == 3:
            return self.author_email
        elif self.__count == 4:
            return self.description
        elif self.__count == 5:
            return self.pip_conf
        else:
            raise NotImplementedError()

    def __answer_none(self):
        if self.__count == 0:
            return self.prj_name
        elif self.__count == 1:
            return self.author_name
        elif self.__count == 2:
            return self.author_email
        elif self.__count == 3:
            return self.description
        elif self.__count == 4:
            return self.pip_conf
        else:
            raise NotImplementedError()

    def __input(self, answer):
        self.__count += 1
        if self.__count == 0 and answer is not None:
            return answer
        if answer is not None:
            return self.__answer_is_not_none()
        return self.__answer_none()

    def run_test(self, answer, agree, folders):
        utils.create(folders)
        _internal_utils.input_ = lambda _: self.__input(answer=answer)

        methods.init(agree=agree, src_path=tests.src_path, dst_path=tests.dst_path)
