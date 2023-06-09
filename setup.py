#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Russell Hrubesky",
    author_email='aetheriak@proton.me',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A generic API client library to quickly create API clients[D[D[D[D[D[D[D[D[D[D[D[D[D[D",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='api_client_generic',
    name='api_client_generic',
    packages=find_packages(include=['api_client_generic', 'api_client_generic.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AETH-erial/api_client_generic',
    version='1.0.0',
    zip_safe=False,
)
