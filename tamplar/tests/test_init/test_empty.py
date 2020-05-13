import pytest

from tamplar import tests
from tamplar.__internal import init
from tamplar.tests import utils, test_init


@pytest.fixture(scope='function', autouse=True)
def fixture():
    init.default_pip_conf = f'{tests.src_path}../pip.conf'
    utils.clean(tests.src_path)
    yield
    utils.clean(tests.src_path)


def test_init_default_yes():
    prj_name = 'prj_name'
    answer = None
    agree = None
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_init_invalid_prj_name():
    prj_name = 'prj+_name'
    answer = None
    agree = None
    folders = []

    with pytest.raises(AssertionError):
        test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_empty(tests.src_path)


def test_init__space_prj_name():
    prj_name = 'prj name'
    answer = None
    agree = None
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name.replace(' ', '_'))


def test_init_line_prj_name():
    prj_name = 'prj-name'
    answer = None
    agree = None
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name.replace('-', '_'))


def test_init_agree_invalid():
    prj_name = None
    answer = None
    agree = 'yes'
    folders = []

    with pytest.raises(AssertionError):
        test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_empty(tests.src_path)


def test_init_agree_yes():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_init_agree_no():
    prj_name = 'prj_name'
    answer = None
    agree = 'n'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_check_service_name():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)
    test_init.assert_service_name(tests.src_path, prj_name=prj_name)


def test_init_author_name():
    prj_name = 'prj_name'
    author_name = 'author_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name, author_name=author_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_info(tests.src_path, validates={'name': prj_name, 'author': author_name})


def test_init_author_email():
    prj_name = 'prj_name'
    author_email = 'author_email'
    answer = None
    agree = 'y'
    folders = [tests.src_path + '1']

    test_init.Core(prj_name=prj_name, author_email=author_email).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_info(tests.src_path, validates={'name': prj_name, 'author_email': author_email})


def test_init_description():
    prj_name = 'prj_name'
    description = 'description'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name, description=description).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_info(tests.src_path, validates={'name': prj_name, 'description': description})


def test_init_pip_conf():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_pip_conf(tests.src_path, pip_conf_path=init.default_pip_conf)


def test_init_enter_pip_conf():
    pip_conf_path = init.default_pip_conf
    init.default_pip_conf = '1'  # failure pip_conf

    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name, pip_conf=pip_conf_path).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_pip_conf(tests.src_path, pip_conf_path=pip_conf_path)


def test_init_docker_compose():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_docker_compose_full(tests.src_path)


def test_init_envs():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_envs(tests.src_path)


def test_init_gitignore():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core(prj_name=prj_name).run_test(answer=answer, agree=agree, folders=folders)

    test_init.assert_gitignore_tamplar(tests.src_path)
