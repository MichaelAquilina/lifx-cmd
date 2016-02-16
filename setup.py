#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'pylifx==0.0.3',
    'bitstring>=3.1.3',
    'netifaces>=0.10.4',
]

setup(
    name='lifx-cmd',
    version='0.2.3',
    description="LifX command line utility to change the state of your lifx bulb. Supports powering on/off, changing RGB/HSB color and temperature.",
    long_description=readme + '\n\n' + history,
    author="Michael Aquilina",
    author_email='michaelaquilina@gmail.com',
    url='https://github.com/MichaelAquilina/lifx-cmd',
    packages=[],
    scripts=['bin/lifx', 'bin/lifx-discover'],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='lifx-cmd',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
