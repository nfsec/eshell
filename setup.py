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
    version = '0.3.7',
    description = 'Elasticsearch interactive shell',
    long_description = readme,
    author = 'Patryk Krawaczyński',
    author_email = 'agresor@nfsec.pl',
    url = 'https://bitbucket.org/agresor/elasticshell',
    license = 'Apache License (2.0)',
    keywords = 'elasticsearch shell',
    install_requires = required,
    zip_safe = False,
    scripts = ['eshell'],
    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Shells'
    )
)
