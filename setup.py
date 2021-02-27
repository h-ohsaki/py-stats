#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-stats",
    version="0.1",
    author="Hiroyuki Ohsaki",
    author_email="ohsaki@lsnl.jp",
    description="calcurate statistics of values in each column",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h-ohsaki/py-stats",
    packages=setuptools.find_packages(),
    install_requires=['perlcompat'],
    scripts=['stats'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)