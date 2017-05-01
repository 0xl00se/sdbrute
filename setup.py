#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

setup(
    name = 'sdbrute',
    version = '1.0.0',
    author = '0xl00se',
    py_modules = ['sdbrute'],
    url = 'https://0xl00se.wordpress.com/',
    install_requires = ['requests'],
    license = 'MIT',
    description = 'A multi-threaded, efficient domain crack tool',
)