import sys
import os
import re

# need to kill off link if we're in docker builds
if os.environ.get('PYTHON_BUILD_DOCKER', None) == 'true':
    del os.link

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def read(fname):
    return open(fname).read()

# On Python 3, we can't "from hamcrest import __version__" (get ImportError),
# so we extract the variable assignment and execute it ourselves.
fh = open('src/hamcrest/__init__.py')
try:
    for line in fh:
        if re.match('__version__.*', line):
            exec(line)
finally:
    if fh:
        fh.close()

extra_attributes = {}
# if sys.version_info >= (3,):
#     extra_attributes['use_2to3'] = True

params = dict(
    name='PyHamcrest',
    version=__version__,  #flake8:noqa
    author='Chris Rose',
    author_email='offline@offby1.net',
    description='Hamcrest framework for matcher objects',
    license='New BSD',
    platforms=['All'],
    keywords='hamcrest matchers pyunit unit test testing unittest unittesting',
    url='https://github.com/hamcrest/PyHamcrest',
    download_url='http://pypi.python.org/packages/source/P/PyHamcrest/PyHamcrest-%s.tar.gz' % __version__,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    provides=['hamcrest'],
    long_description=read('README.rst'),
    install_requires=['six'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
    **extra_attributes
    )

all_params = dict(params.items(), **extra_attributes)
setup(**all_params)
