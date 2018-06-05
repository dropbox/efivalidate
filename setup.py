#!/usr/bin/env python

from distutils.core import setup

setup(name='efivalidate',
      version='1.0',
      description='Apple firmware validation tool',
      author='Rick Mark',
      author_email='rickmark@dropbox.com',
      url='https://github.com/dropbox/efivalidate',
      packages=['distutils', 'distutils.command'],
     )