import enum
import os
import string
from collections import namedtuple

from tamplar.__internal import utils

from jinja2 import Template


class DockerCompose(enum.Enum):
    Started = 0
    AlreadyWorks = 1


repo_name = 'python-service-layout'
account = 'git://github.com/Hedgehogues'
default_pip_conf = os.path.expanduser('~')+'/.pip/pip.conf'


InitParams = namedtuple('InitParams', ['pkg_name', 'author', 'author_email', 'description', 'pip_conf_path'])


def init_gitignore(src_path=None):
    if src_path is None:
        src_path = '.'
    with open(src_path+'.gitignore', 'a') as fd:
        fd.write(utils.tamplar_config)
        fd.write('\n')


def name_validator(project_name):
    name_symbols = set(project_name.lower())
    all_symbols = string.ascii_lowercase + string.digits + ' -_'
    intersection = name_symbols.difference(all_symbols)
    assert len(intersection) == 0, 'invalid project name'


def package_name(name):
    return name.replace('-', '_').replace(' ', '_')


def init_params():
    pkg_name = utils.input_('please enter project name (available letters: digits, latin alphanum, -, _, space): ')
    assert len(pkg_name) > 0, 'project name must be not empty'
    name_validator(pkg_name)
    author_name = utils.input_('please enter author name: ')
    author_email = utils.input_('please enter author\'s email name: ')
    description = utils.input_('please enter description of service: ')
    pip_conf_path = utils.input_('please pip.conf path (default: ~/.pip/pip.conf). You can read about pip conf here ('
                                 'shorturl.at/CJP01): ')
    if len(pip_conf_path) == 0:
        pip_conf_path = default_pip_conf
    return InitParams(pkg_name=pkg_name, author=author_name, author_email=author_email, description=description,
                      pip_conf_path=pip_conf_path)


def init_readme(path, params):  # TODO: not tested (.gitkeep not checked)
    for root, dirs, files in os.walk(path):
        with open(f'{root}/.gitkeep', 'w') as fd:
            fd.write('')
        for name in files:
            if name != 'README.md':
                continue
            os.remove(os.path.join(root, name))
    os.remove(path + '.gitkeep')
    with open(path+'README.md', 'w') as fd:
        fd.write(f'# {params.pkg_name}\n')


def init_package(params, src_path, dst_path):  # TODO: Not tested (package name not checked)
    src_path_new = os.path.abspath(f'{src_path}{repo_name}/')
    utils.mv(src=src_path_new, dst=dst_path)
    pkg_name = package_name(params.pkg_name)
    pkg_src_path = f'{src_path}{repo_name.replace("-", "_")}/'
    pkg_dst_path = f'{dst_path}{pkg_name}/'
    utils.mv(src=pkg_src_path, dst=pkg_dst_path)


def fill_template(f, params):
    if f[-5:] != '.tmpl':
        return
    os.rename(f, f[:-5])
    with open(f[:-5]) as fd:
        lines = fd.read()
    template = Template(lines)
    lines = str(template.render(**dict(params._asdict())))
    with open(f[:-5], 'w') as fd:
        fd.write(lines)


def init_templates(params, path):
    from pathlib import Path
    files = []
    for p in Path(path).rglob('*'):
        path_ = str(p.parent)
        if path_.find('.git') != -1:
            continue
        files.append(f'{str(p.parent)}/{p.name}')
    for f in files:
        fill_template(f, params)

