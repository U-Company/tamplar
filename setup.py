import setuptools

import version


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()

install_reqs = parse_requirements('./requirements')
print(install_reqs)

dscr = "This util creates new service of python. This one has some additional command cli for control of development"

setuptools.setup(
    name=version.app_name,
    version=version.app_version,
    author="Urvanov Egor",
    author_email="hedgehogues@bk.ru",
    description=dscr,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hedgehogues/tamplar",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    package_data={'': ['__cmd/*', '__internal/*']},
    install_requires=install_reqs,
    entry_points={
        'console_scripts': [
            'tamplar=tamplar.__cmd.main:main',
        ],
    },
)

