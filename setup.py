#!/usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.1.2"
description = (
    "Supports encoding conversion between `unicode` and `ibm935`",
)

long_description = open("README.md", "rb").read().decode("utf-8")

classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name="ibm935",
    version=version,
    description=description,
    long_description=long_description,
    license="MIT",
    author="Eric Wong",
    author_email="ericwong@zju.edu.cn",
    url="https://github.com/littlefisher/ibm935",
    classifiers=classifiers,
    py_modules=['ibm935'],
)
