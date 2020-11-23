#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':

    setup(
        name='azure-cli-local',
        version='0.1',
        description='Thin wrapper around the Azure CLI for use with LocalStack',
        author='Waldemar Hummer',
        author_email='waldemar.hummer@gmail.com',
        url='https://github.com/localstack/azure-cli-local',
        packages=[],
        scripts=['bin/azlocal', 'bin/azlocal.bat'],
        package_data={},
        data_files={},
        install_requires=['azure-cli'],
        license="Apache License 2.0",
        classifiers=[
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: Apache Software License",
            "Topic :: Software Development :: Testing"
        ]
    )
