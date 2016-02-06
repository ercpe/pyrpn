#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name='pyrpn',
	version='0.1',
	description='Python implementation of a reverse polish notation parser',
	author='Johann Schmitz',
	author_email='johann@j-schmitz.net',
	url='https://ercpe.de/projects/pyrpn',
	#download_url='',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	include_package_data=True,
	zip_safe=False,
	license='GPL-3',
)