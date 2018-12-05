import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='stevesie',
    version='0.0.5', # Don't forget to update release.sh
    author='Stevesie, LLC',
    author_email='steve@stevesie.com',
    description='Stevesie Python Client.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/stevesie/stevesie-py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'inflection>=0.2.0,<1.0',
        'python-dateutil>=2.0,<3.0',
        'requests>=0.11.1,<3.0'
    ]
)
