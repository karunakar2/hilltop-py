# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

# General parameters
name = 'hilltop-py'
main_package = 'hilltoppy'
# datasets = 'datasets'
version = '1.5.0'
descrip = 'Functions to access Hilltop data'

# The below code is for readthedocs. To have sphinx/readthedocs interact with
# the contained package, readthedocs needs to build the package. But the dependencies
# should be installed via the conda yml env file rather than during the package build.
if os.environ.get('READTHEDOCS', False) == 'True':
    INSTALL_REQUIRES = []
else:
    INSTALL_REQUIRES = ['pandas']

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name=name,
    version=version,
    description=descrip,
    url=f'https://github.com/mullenkamp/{name}',
    author='Mike Kittridge',
    author_email='mullenkamp1@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',
        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='hilltop',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests', '__pycashe__']
    ),
    install_requires=INSTALL_REQUIRES,
    license='Apache',
)
