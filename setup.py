# -*- coding: utf-8 -*-
from setuptools import setup

requires = [
    "numpy"
]

setup(
    name="irmet",
    version="0.1",
    description="A set of functions that calculate various metrics in Information Retrieval.",
    url="https://github.com/moriaki3193/irmet",
    author="moriaki3193",
    author_email="moriaki3193@gmail.com",
    license="MIT",
    keywords="metrics information retrieval",
    packages=[
        "irmet",
    ],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
)
