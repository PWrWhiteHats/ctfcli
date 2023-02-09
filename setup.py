# -*- coding: utf-8 -*-
import os
import re

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup


with open("ctfcli/__init__.py") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname), "r") as fp:
            return fp.read().strip()
    except IOError:
        return ""


setup(
    name="ctfcli",
    version=version,
    author="Kevin Chung",
    author_email="kchung@ctfd.io",
    license="Apache 2.0",
    description="Tool for creating and running Capture The Flag competitions",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords=["ctf"],
    classifiers=[],
    zip_safe=False,
    install_requires=[
        "cookiecutter==2.1.1",
        "click==8.1.3",
        "fire==0.2.1",
        "pyyaml==6.0",
        "Pygments==2.14.0",
        "requests==2.28.2",
        "colorama==0.4.6",
        "appdirs==1.4.4",
        "python-frontmatter==1.0.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["ctf = ctfcli.__main__:main"]},
)
