
"""
To install the library, run the following

python setup.py install

prerequisite: setuptools
http://pypi.python.org/pypi/setuptools

get the dependencies and installs

"""
from setuptools import find_packages, setup



with open("requirements.txt", encoding="utf-8") as f:
    INSTALL_REQUIRES = [x.strip() for x in f.read().split("\n")]

setup(
    name="md2tex",
    version="0.0.0",
    description="Markdown to LaTeX converter",
    author="Pratik Shrestha (prtx)",
    py_modules=["md2tex"],
    packages=find_packages(),
    package_data={"md2tex": ["templates/*jinja"]},
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "md2tex = md2tex.cli:main"
        ]
    }
)
