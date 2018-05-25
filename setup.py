# -*- coding: utf-8 -*-


from setuptools import setup

import requests_mauth

setup(
    name='requests_mauth',
    version=requests_mauth.__version__,
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
