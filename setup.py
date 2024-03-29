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
    version = '0.7.10.2',
    description = 'Elasticsearch API available via Python interactive shell.',
    long_description = readme,
    author = 'Patryk Krawaczyński',
    author_email = 'github@nfsec.pl',
    url = 'https://github.com/nfsec/eshell',
    license = 'Apache License (2.0)',
    keywords = 'elasticsearch shell administrator terminal cluster managment',
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
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Shells'
    )
)
