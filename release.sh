#!/usr/bin/env bash

VERSION='0.0.7' # Don't forget to update setup.py

python setup.py sdist bdist_wheel
twine upload dist/*

git tag $VERSION
git push origin $VERSION
