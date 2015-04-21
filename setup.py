import os
from setuptools import setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="subgit",
    version="0.1",
    author="Ce Gao",
    author_email="gaoce@coe.neu.edu",
    description=("Download a sub folder or file from github.com"),
    license="MIT",
    packages=['subgit'],
    long_description=read('README.md'),
    entry_points={'console_scripts': ['subgit = subgit.subgit:main']}
)
