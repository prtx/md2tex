
"""
To install the library, run the following

python setup.py install

prerequisite: setuptools
http://pypi.python.org/pypi/setuptools

get the dependencies and installs

"""
from setuptools import find_packages, setup

import md2tex


with open("requirements.txt", encoding="utf-8") as f:
    INSTALL_REQUIRES = [x.strip() for x in f.read().split("\n")]


setup(
    name=md2tex.__PKG_NAME__,
    version=md2tex.__version__,
    description=md2tex.__PKG_DESC__,
    author=md2tex.__AUTHOR__,
    py_modules=["md2tex"],
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
)
