#!/usr/bin/env bash

VERSION='0.0.2'

python setup.py sdist bdist_wheel
twine upload dist/*

git tag $VERSION
git push origin $VERSION
