#!/usr/bin/env python
"""
Install django-enumchoicefield using setuptools
"""
from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    readme = f.read()

with open('enumchoicefield/version.py') as v:
    version = '0.0.0'
    exec(v.read())  # Get version


setup(
    name='django-enumchoicefield',
    version=version,
    description='A choice field for Django using native Python Enums',
    long_description=readme,
    author='Tim Heap',
    author_email='tim@takeflight.com.au',
    url='https://github.com/takeflight/django-enumchoicefield',

    install_requires=['Django>=1.8'],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
