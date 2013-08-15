#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(name = 'idcard',
      version = '0.1',
      description = 'get information from id card number',
      url = 'http://github.com/exherb/idcard',
      author = 'Michael Herb',
      author_email = 'i@4leaf.me',
      license = 'LICENCE',
      packages = ['idcard'],
      package_data = {'idcard': ['areas.json']},
      zip_safe = False)
