#!/usr/bin/env python

from setuptools import setup

setup(
    name='PWI EGZ',
    version='1.0',
    description='Egzamin z PWI',
    author='Moje Imie',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django<=1.4','django-celery','django-kombu','django-registration','requests','couchdb'],
)
