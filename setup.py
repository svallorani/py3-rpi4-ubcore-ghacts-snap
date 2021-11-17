from setuptools import setup
import sys,os

setup(
    name = 'py3_rpi4_ubcore_ghacts_snap',
    version = '0.1.0',
    description = 'Prova di flusso di lavoro CI/CD su progetto Linux Embedded scritto in Python 3 - usando RaspberryPi 4 - con Ubuntu Core, GitHub Actions, Snapcraft',
    license='MIT',
    author = 'Silvio Vallorani',
    packages = ['src'],
    package_data={'src': ['description.txt']
                 },
    install_requires=['future'],
    entry_points = {
        'console_scripts': [
            'hello=src.app:main']
            },
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: MIT License',],
)
