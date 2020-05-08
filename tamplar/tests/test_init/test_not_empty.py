import pytest

from tamplar import tests
from tamplar.tests import utils, test_init


@pytest.fixture(scope='function', autouse=True)
def fixture():
    utils.clean(tests.src_path)
    yield
    utils.clean(tests.src_path)


def test_init_no():
    prj_name = None
    answer = 'n'
    agree = None
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_exist_folder(folders[0])


def test_init_NO():
    prj_name = None
    answer = 'N'
    agree = None
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_exist_folder(folders[0])


def test_init_invalid():
    prj_name = None
    answer = 'yes'
    agree = None
    folders = [tests.src_path + '1']

    with pytest.raises(AssertionError):
        test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_exist_folder(folders[0])


def test_init_yes():
    prj_name = 'prj_name'
    answer = 'y'
    agree = None
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)
    test_init.assert_exist_folder(folders[0], not_=True)


def test_init_YES():
    prj_name = 'prj_name'
    answer = 'Y'
    agree = None
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)
    test_init.assert_exist_folder(folders[0], not_=True)


def test_init_none():
    prj_name = 'prj_name'
    answer = ''
    agree = None
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)
    test_init.assert_exist_folder(folders[0], not_=True)


def test_init_prj_name_empty():
    prj_name = ''
    answer = ''
    agree = None
    folders = [tests.src_path + '1']

    with pytest.raises(AssertionError):
        test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_empty(tests.src_path)


def test_init_agree_invalid():
    prj_name = None
    answer = None
    agree = 'yes'
    folders = [tests.src_path + '1']

    with pytest.raises(AssertionError):
        test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_exist_folder(tests.src_path)


def test_init_agree_yes():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name)
    test_init.assert_exist_folder(folders[0], not_=True)


def test_init_agree_no():
    prj_name = 'prj_name'
    answer = None
    agree = 'n'
    folders = [tests.src_path + '1']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_exist_folder(folders[0])


def test_init_idea():
    prj_name = 'prj_name'
    answer = None
    agree = 'y'
    folders = [tests.src_path + '.idea']

    test_init.Core().run_test(answer=answer, prj_name=prj_name, agree=agree, folders=folders)

    test_init.assert_validate_layout(tests.src_path, prj_name=prj_name, additional=['.idea'])
