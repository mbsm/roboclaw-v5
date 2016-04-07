import os
import sys

from setuptools import setup, find_packages

setup(
	name='rcv5',
	version='1.0',
	url='https://github.com/plusk01/roboclaw-v5',
	description=('Python library for RoboClaw v5'),
	author='Parker Lusk',
	author_email='parkerclusk@gmail.com',
	license='MIT',
	packages=find_packages(exclude=['examples']),
	install_requires=['pyserial'],
)
