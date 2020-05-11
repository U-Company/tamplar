import os
import string
from collections import namedtuple

from tamplar.__internal import utils


repo_name = 'python-service-layout'
account = 'git://github.com/Hedgehogues'


InitParams = namedtuple('InitParams', ['prj_name', 'author_name', 'author_email', 'description', 'pip_conf_path'])


def name_validator(project_name):
    name_symbols = set(project_name.lower())
    all_symbols = string.ascii_lowercase + string.digits + ' -_'
    intersection = name_symbols.difference(all_symbols)
    assert len(intersection) == 0, 'invalid project name'


def package_name(name):
    return name.replace('-', '_').replace(' ', '_')


def init_params():
    prj_name = utils.input_('please enter project name (available letters: digits, latin alphanum, -, _, space): ')
    assert len(prj_name) > 0, 'project name must be not empty'
    name_validator(prj_name)
    author_name = utils.input_('please enter author name: ')  # TODO:  not tested
    author_email = utils.input_('please enter author\'s email name: ')  # TODO: not tested
    description = utils.input_('please enter description of service: ')  # TODO:  not tested
    pip_conf_path = utils.input_('please pip.conf path (default: ~/.pip/pip.conf). You can read about pip conf here ('
                                 'shorturl.at/CJP01): ') # not tested
    if len(pip_conf_path) == 0:  # not tested
        pip_conf_path = '/.pip/pip.conf'
    return InitParams(prj_name=prj_name, author_name=author_name, author_email=author_email, description=description,
                      pip_conf_path=pip_conf_path)


def init_readme(path, params):
    for root, dirs, files in os.walk(path):  # TODO: not tested
        with open(f'{root}/.gitkeep', 'w') as fd:
            fd.write('')
        for name in files:
            if name != 'README.md':
                continue
            os.remove(os.path.join(root, name))
    os.remove(path + '.gitkeep')
    with open(path+'README.md', 'w') as fd:  # TODO: not tested
        fd.write(f'# {params.prj_name}\n')  # TODO: not tested


def init_tmpl(params, path):
    os.rename(f'{path}setup.tmpl', f'{path}setup.py')
    os.rename(f'{path}info.tmpl', f'{path}info.py')
    with open(f'{path}info.py') as fd:
        lines = fd.read()
    with open(f'{path}info.py', 'w') as fd:
        lines = lines.replace('{{prj_name}}', params.prj_name)
        lines = lines.replace('{{author}}', params.author_name)
        lines = lines.replace('{{author_email}}', params.author_email)
        lines = lines.replace('{{description}}', params.description)
        fd.write(lines)


def init_package(params, src_path, dst_path):
    src_path_new = os.path.abspath(f'{src_path}{repo_name}/')
    utils.mv(src=src_path_new, dst=dst_path)
    pkg_name = package_name(params.prj_name)
    pkg_src_path = f'{src_path}{repo_name.replace("-", "_")}/'
    pkg_dst_path = f'{dst_path}{pkg_name}/'
    utils.mv(src=pkg_src_path, dst=pkg_dst_path)