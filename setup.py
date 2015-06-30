# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='ThreeScalePY',
    version='2.5',
    description='Client for the 3scale API',
    author='3scale',
    author_email='support@3scale.net',
    url='http://www.3scale.net',
    license='MIT',
    py_modules=['ThreeScalePY'],
    install_requires=[
      'httpretty==0.8.6'
    ]
)

