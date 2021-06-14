# -*- coding: utf-8 -*-
"""Setup file for the avaframe package.
   Adapted from the Python Packaging Authority template."""

from setuptools import setup, find_packages  # Always prefer setuptools


DISTNAME = 'myMod'

setup(
    # Project info
    name=DISTNAME,
    version='dev',
    packages=find_packages(exclude=['docs']),
    # Include package data
    include_package_data=True,
)
