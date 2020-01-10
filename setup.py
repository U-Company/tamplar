import setuptools


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()

install_reqs = parse_requirements('./requirements')
print(install_reqs)

setuptools.setup(
    name="my_package",
    version="0.1.0",
    author="Author",
    author_email="author@author.author",
    description="This is short readme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hedgehogues/docker-compose-deploy",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=install_reqs,
)
