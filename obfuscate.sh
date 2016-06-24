#!/usr/bin/env bash
set -e

PROJECT_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PYTHONPATH=${PROJECT_DIRECTORY} python2 ${PROJECT_DIRECTORY}/ohirods/obfuscate.py $1