# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


desc = 'irmet - A set of METrics for Information Retrieval.'

setup(
    name='irmet',
    version='0.2.1',
    description=desc,
    url='https://github.com/moriaki3193/irmet',
    author='Moriaki Saigusa',
    author_email='moriaki3193@gmail.com',
    license=license,
    keywords='metrics information retrieval',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['numpy'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    zip_safe=False,
)
