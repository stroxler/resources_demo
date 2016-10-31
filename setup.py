import os
from setuptools import setup

PACKAGE = 'resources_demo'


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name=PACKAGE,
      version='0.0.1',
      description=(
          'Tools for working with container types, command data operations, '
          'and concise exception handling'
      ),
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='',
      url='https://github.com/stroxler/resources_demo',
      author='Steven Troxler',
      author_email='steven.troxler@gmail.com',
      license='MIT',
      packages=[PACKAGE],
      package_data={'resources_demo': ['internal_resources/*.txt']},
      include_package_data=True,
      zip_safe=False)
