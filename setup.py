#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os

try:
  from setuptools import setup
  from setuptools import find_packages

except ImportError:
  from distutils.core import setup
  from distutils.core import find_packages


def get_requires (requirements_filename):
  '''
  What packages are required for this module to be executed?

  Parameters
  ----------
    requirements_filename : str
      filename of requirements (e.g requirements.txt)

  Returns
  -------
    requirements : list
      list of required packages
  '''
  with open(requirements_filename, 'r') as fp:
    requirements = fp.read()

  return list(filter(lambda x: x != '', requirements.split()))


def read_description (readme_filename):
  '''
  Description package from filename

  Parameters
  ----------
    readme_filename : str
      filename with readme information (e.g README.md)

  Returns
  -------
    description : str
      str with description
  '''

  try:

    with open(readme_filename, 'r') as fp:
      description = '\n'
      description += fp.read()

    return description

  except IOError:
    return ''



here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = 'anonymize-slide'
DESCRIPTION = 'Remove the slide label from whole-slide images'
URL = 'https://github.com/Nico-Curti/anonymize-slide'
EMAIL = ['nico.curti2@unibo.it']
AUTHOR = ['Benjamin Gilbert', 'Nico Curti']
REQUIRES_PYTHON = '>=2.7'
VERSION = None
KEYWORDS = 'whole-slide WSI anonymizer'

README_FILENAME = os.path.join(here, 'README.md')
REQUIREMENTS_FILENAME = os.path.join(here, 'requirements.txt')
VERSION_FILENAME = os.path.join(here, '__version__.py')

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
  LONG_DESCRIPTION = read_description(README_FILENAME)

except IOError:
  LONG_DESCRIPTION = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
  with open(VERSION_FILENAME) as fp:
    exec(fp.read(), about)

else:
  about['__version__'] = VERSION

# parse version variables and add them to command line as definitions
Version = about['__version__'].split('.')


setup(
  name                          = NAME,
  version                       = about['__version__'],
  description                   = DESCRIPTION,
  long_description              = LONG_DESCRIPTION,
  long_description_content_type = 'text/markdown',
  author                        = AUTHOR,
  author_email                  = EMAIL,
  maintainer                    = AUTHOR,
  maintainer_email              = EMAIL,
  python_requires               = REQUIRES_PYTHON,
  install_requires              = get_requires(REQUIREMENTS_FILENAME),
  url                           = URL,
  download_url                  = URL,
  keywords                      = KEYWORDS,
  packages                      = find_packages(include=['*'], exclude=('test', 'testing')),
  include_package_data          = True, # no absolute paths are allowed
  entry_points                  = {'console_scripts': ['anonymize_slide=anonymize_slide:_main']},
  platforms                     = 'any',
  classifiers                   =[
                                   #'License :: OSI Approved :: GPL License',
                                   'Programming Language :: Python',
                                   'Programming Language :: Python :: 3',
                                   'Programming Language :: Python :: 3.6',
                                   'Programming Language :: Python :: Implementation :: CPython',
                                   'Programming Language :: Python :: Implementation :: PyPy'
                                 ],
  license                       = 'GPL'
)
