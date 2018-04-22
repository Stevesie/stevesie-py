from os.path import dirname, join
from setuptools import setup

setup(
    name='Stevesie',
    version='0.0.1',
    description='Stevesie Python client.',
    author='Stevesie, LLC',
    author_email='steve@stevesie.com',
    install_requires=[
        'requests>=0.11.1,<3.0',
        'inflection>=0.2.0,<1.0'
    ]
)
