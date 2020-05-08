import pytest

from tamplar import tests
from tamplar.tests import utils, test_init


@pytest.fixture(scope='function', autouse=True)
def fixture():
    global count
    count = 0
    utils.clean(tests.src_path)
    yield
    utils.clean(tests.src_path)


def test_init_default_yes():
    prj_name = 'prj_name'
    answer = None
    agree = None
    folders = []

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_init_invalid_prj_name():
    prj_name = 'prj+_name'
    answer = None
    agree = None
    folders = []

    with pytest.raises(AssertionError):
        test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_empty(tests.src_path)


def test_init__space_prj_name():
    prj_name = 'prj name'
    answer = None
    agree = None
    folders = []

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name.replace(' ', '_'))


def test_init_line_prj_name():
    prj_name = 'prj-name'
    answer = None
    agree = None
    folders = []

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name.replace('-', '_'))


def test_init_agree_invalid():
    prj_name = None
    answer = None
    agree = 'yes'
    folders = []

    with pytest.raises(AssertionError):
        test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_empty(tests.src_path)


def test_init_agree_yes():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = []

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_init_agree_no():
    prj_name = 'prj_name'
    answer = None
    agree = 'n'
    folders = []

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)


def test_check_service_name():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = [tests.src_path + '.idea']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name, additional=['.idea'])
    test_init.assert_service_name(tests.src_path, prj_name=prj_name)
