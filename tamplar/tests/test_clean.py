import os

import pytest

from tamplar import tests
from tamplar.api import methods
from tamplar.tests import utils


@pytest.fixture(scope='function', autouse=True)
def fixture():
    utils.clean(tests.src_path)
    yield
    utils.clean(tests.src_path)


def assert_deleted(folders):
    for f in folders:
        assert not os.path.isdir(f)


def assert_existed(folders):
    for f in folders:
        assert os.path.isdir(f)


def test_clean_not_found_files():
    methods.clean(tests.src_path)


def test_clean_one_file():
    not_deleted = [tests.src_path + 'not-delete']
    deleted = [tests.src_path + 'build']
    utils.create(not_deleted + deleted)

    methods.clean(tests.src_path)

    assert_deleted(deleted)
    assert_existed(not_deleted)


def test_clean_egg_info():
    not_deleted = [tests.src_path + 'not-delete']
    deleted = [tests.src_path + 'xxx.egg-info']
    utils.create(not_deleted + deleted)

    methods.clean(tests.src_path)

    assert_deleted(deleted)
    assert_existed(not_deleted)


def test_clean_all_files():
    not_deleted = [tests.src_path + 'not-delete']
    deleted = [tests.src_path + 'build', tests.src_path + 'dist', tests.src_path + 'test.egg-info']
    utils.create(not_deleted + deleted)

    methods.clean(tests.src_path)

    assert_deleted(deleted)
    assert_existed(not_deleted)
