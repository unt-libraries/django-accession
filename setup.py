#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-accession',
    version='0.9.0',
    packages=find_packages(exclude=['tests*']),
    description='',
    long_description='See the home page for more information.',
    include_package_data=True,
    install_requires=[
        'django-localflavor>=1.0',
        'django-databrowse>=1.3'
    ],
    url='https://github.com/unt-libraries/django-accession',
    author='University of North Texas Libraries',
    author_email='mark.phillips@unt.edu',
    license='BSD',
    keywords=['django', 'fashion', 'app'],
    classifiers=[
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.6',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
