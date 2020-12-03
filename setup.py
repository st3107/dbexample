from os import path
from setuptools import setup, find_packages
import sys


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 7)
if sys.version_info < min_version:
    error = """
dbexample does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='dbexample',
    version='0.2.1',
    description="An example nsls-ii database that can be accessed by the databroker.",
    long_description=readme,
    author="Songsheng Tao",
    author_email='st3107@columbia.edu',
    url='https://github.com/st3107/dbexample',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    py_modules=['example'],
    entry_points={'intake.catalogs': ['example = dbexample.example:catalog_instance']},
    include_package_data=True,
    package_data={
        'dbexample': [
            "data/*"
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
