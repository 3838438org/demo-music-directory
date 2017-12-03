# This file is autogenerated by medikit code generator.
# All changes will be overwritten.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'mused/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='',
    author_email='',
    description='Music directory demo / Bonobo ETL',
    license='A2PL',
    name='mused',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=[
        'bonobo', 'Jinja2 (>= 2.10, < 2.11)', 'SPARQLWrapper (~= 1.8.0)', 'bonobo', 'brotli (>= 1.0, < 1.1)',
        'django (>= 2.0, < 2.1)', 'django-extensions (>= 1.9, < 1.10)', 'django_includes (~= 0.2.0)',
        'psycopg2 (~= 2.7.3)', 'requests-cache (~= 0.4.13)', 'whitenoise (== 4.0b4)'
    ],
    extras_require={
        'dev': ['django-debug-toolbar (>= 1.8, < 1.9)', 'django-extensions (>= 1.9, < 1.10)', 'yapf'],
        'prod': ['gunicorn (== 19.7.1)']
    },
    url='',
    download_url=''.format(version=version),
)
