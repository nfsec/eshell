#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = 'eshell',
    version = '0.6.8.2',
    description = 'Elasticsearch interactive shell',
    long_description = readme,
    author = 'Patryk Krawaczyński',
    author_email = 'github@nfsec.pl',
    url = 'https://github.com/nfsec/eshell',
    license = 'Apache License (2.0)',
    keywords = 'elasticsearch shell terminal managment',
    install_requires = required,
    data_files=[('', ['LICENSE', 'README.md'])],
    zip_safe = False,
    scripts = ['eshell'],
    classifiers = (
        'Development Status :: 5',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Shells'
    )
)
