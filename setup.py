# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


desc = 'irmet - A set of METrics for Information Retrieval.'

setup(
    name='irmet',
    version='0.2',
    description=desc,
    url='https://github.com/moriaki3193/irmet',
    author='moriaki3193',
    author_email='moriaki3193@gmail.com',
    license=license,
    keywords='metrics information retrieval',
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests'
)
