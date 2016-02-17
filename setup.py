#! /usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-accession',
    version='1.1.2',
    packages=find_packages(exclude=['tests*']),
    description='',
    long_description='See the home page for more information.',
    include_package_data=True,
    install_requires=[
        'django-localflavor>=1.0',
        'django-queryset-csv>=0.3.1',
    ],
    zip_safe=False,
    url='https://github.com/unt-libraries/django-accession',
    author='University of North Texas Libraries',
    author_email='mark.phillips@unt.edu',
    license='BSD',
    keywords=['django', 'fashion', 'app'],
    classifiers=[
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ]
)
