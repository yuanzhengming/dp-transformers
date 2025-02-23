# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from setuptools import setup, find_packages

version = '1.0.1'

with open('README.md',encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dp-transformers',
    version=version,
    description='Differentially-private transformers using HuggingFace and Opacus',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://www.github.com/microsoft/dp-transformers",
    author='Microsoft',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires=">=3.7.0",
    include_package_data=True,
    extras_require={
        "test": [
            "pytest",
            "loralib"
        ]
    },
    install_requires=[
        "transformers>=4.20.1,<=4.28.1",
        "datasets>=2.0.0,<=2.6.1",
        "opacus>=1.1.3,<1.3.0",
        "prv-accountant<0.2.0",
        "torch>=1.9.1,<1.13.0",
    ],
    test_suite="tests",
    zip_safe=False
)
