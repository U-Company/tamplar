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


def assert_count_folders(folder, count_):
    assert len(os.listdir(folder)) == count_


def assert_validate_layout(folder, prj_name, additional=None):
    if additional is None:
        additional = []
    files = ['setup.py', 'info.py', 'requirements', 'README.md', 'makefile', '.gitignore', 'tests', 'service',
             'scripts', prj_name, 'logs', 'docs', 'deployments', 'data', 'configs', '.git'] + additional
    assert sorted(files) == sorted(os.listdir(folder))


def assert_service_name(folder, prj_name):
    with open(folder+'info.py', 'r') as fd:
        assert fd.read().find(prj_name) >= 0


# check service name


class Core:
    def __init__(self):
        self.__count = 0

    def __input(self, prj_name, answer):
        if self.__count == 0 and answer is not None:
            self.__count += 1
            return answer
        return prj_name

    def run_test(self, answer, prj_name, agree, folders):
        utils.create(folders)
        _internal_utils.input_ = lambda _: self.__input(prj_name=prj_name, answer=answer)

        methods.init(agree=agree, src_path=tests.src_path, dst_path=tests.dst_path)
