# -*- coding: utf-8 -*-
__author__ = 'isparks'

import re
from setuptools import setup

init = open('requests-mauth/__init__.py').read()
version = re.search("__version__ = '([^']+)'", init).group(1)

setup(
    name='requests-mauth',
    version=version,
    author='Ian Sparks',
    author_email='isparks@mdsol.com',
    packages=['requests_mauth'],
    url='https://github.com/mdsol/requests-mauth',
    license='MIT',
    description="An MAuth client based around the excellent requests library.",
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    package_data = { '': ['README.md'] },
    install_requires=['rsa', 'requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
