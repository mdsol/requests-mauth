# -*- coding: utf-8 -*-
import re

from setuptools import setup

init = open('requests_mauth/__init__.py').read()
version = re.search("__version__ = '([^']+)'", init).group(1)

setup(
    name='requests_mauth',
    version=version,
    author='Medidata Solutions',
    author_email='support@mdsol.com',
    packages=['requests_mauth'],
    url='https://github.com/mdsol/requests-mauth',
    license='MIT',
    description="An MAuth client based around the excellent requests library.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.md']},
    install_requires=['rsa', 'requests'],
    test_suite='tests.requests_mauth_suite',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
