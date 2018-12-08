#!/usr/bin/env bash

VERSION='0.0.6' # Don't forget to update setup.py

python setup.py sdist bdist_wheel
twine upload dist/*

git tag $VERSION
git push origin $VERSION
