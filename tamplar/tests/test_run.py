import pytest

from tamplar import tests
from tamplar.__internal import init
from tamplar.api import methods
from tamplar.tests import test_init, utils


@pytest.fixture(scope='function', autouse=True)
def fixture():
    init.default_pip_conf = f'{tests.src_path}/../pip.conf'
    utils.clean(tests.src_path)
    test_init.Core(prj_name='prj_name').run_test(answer=None, agree='y', folders=[])
    methods.kill(src_path=tests.src_path)
    yield
    methods.kill(src_path=tests.src_path)
    utils.clean(tests.src_path)


def assert_status(items, status):
    for k, v in items:
        assert v == status


def test_run_env_started():
    mode = 'env'

    methods.run(src_path=tests.src_path, mode=mode)
    assert_status(methods.codes.items(), init.DockerCompose.Started)


def test_run_env_already_works():
    mode = 'env'

    methods.run(src_path=tests.src_path, mode=mode)
    assert_status(methods.codes.items(), init.DockerCompose.Started)
    methods.run(src_path=tests.src_path, mode=mode)
    assert_status(methods.codes.items(), init.DockerCompose.AlreadyWorks)


def test_run_env_rerun():
    mode = 'env'

    methods.run(src_path=tests.src_path, mode=mode)
    assert_status(methods.codes.items(), init.DockerCompose.Started)
    methods.kill(src_path=tests.src_path)
    methods.run(src_path=tests.src_path, mode=mode)
    assert_status(methods.codes.items(), init.DockerCompose.Started)
