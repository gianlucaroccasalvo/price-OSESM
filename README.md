# Electricity price project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Purpose
This repo and all associated commits are intended as an exercise to practice the GitHub workflow, contestually to the Open Source Energy System Modelling course held by prof Daniel Huppmann at Technische Universitet Wien.

Furthermore, under future proper development, it is desire of the owner to build this project as an advanced package of tools and datasets to observe electricity price values and trends over time.

## Content

Up to date, it contains a simple function able to compute the price of electricity in a closed market using the respective prices and shares of renewable and fossil source electricity production.

It also contains two continuos integration tools:
- stickler-ci to check for style errors and automatically **fix** them, according to pep8 python code style guide and using flake8 linter
- GitHub Actions Python application to automatically run **tests** on the implemented functions, when a change is applied and pushed, using pytest function.

Credits for CONTRIBUTING.rst and PULL_REQUEST_TEMPLATE are due to PYAM project, which has been forked to use a copy of the indicated files.

## License disclaimer
Copyright 2021 Gianluca Roccasalvo

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
