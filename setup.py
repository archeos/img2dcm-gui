#!/usr/bin/env python

from distutils.core import setup

setup(name='img2dcm-gui',
      version='0.1-snapshot',
      description='A simple GUI for img2dcm',
      author='The Archeos Team',
      url='https://github.com/archeos/img2dcm-gui',
      requires=['pyqt (>= 4.9.3)', 'img2dcm (>= 0.1.0)'],
      licence='GPL-2'
     )

