#!/usr/bin/env bash

VERSION='0.0.1'

git tag $VERSION
git push origin $VERSION

python setup.py sdist bdist_wheel
twine upload dist/*
