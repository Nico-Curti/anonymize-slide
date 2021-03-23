# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2021-03-23

First commit on the original fork available [here](https://github.com/bgilbert/anonymize-slide).

### Added

- Add the [pyproject.toml](https://github.com/Nico-Curti/anonymize-slide/blob/master/pyproject.toml) for the build requirements according to PEP-518.
- Add the [setup.py](https://github.com/Nico-Curti/anonymize-slide/blob/master/setup.py) for the module installation.
- Add the [MANIFEST](https://github.com/Nico-Curti/anonymize-slide/blob/master/MANIFEST.in) file.
- Add the [requirements](https://github.com/Nico-Curti/anonymize-slide/blob/master/requirements.txt) file for the dependencies.
- Move the COPYING file to an explicit [LICENSE](https://github.com/Nico-Curti/anonymize-slide/blob/master/LICENSE) file.
- Add the [version](https://github.com/Nico-Curti/anonymize-slide/blob/master/__version__.py) file.
- Add the entry_point in the module for an easy-to-use command line program.
- Add the manual copy of the original file to prevent troubles.

### Fixed

- Fix the Python 3 support for the anonymizers
- Fix command line parser for multi-files or directory
- Change the main filename
