import sys
import os
import re

# need to kill off link if we're in docker builds
if os.environ.get('PYTHON_BUILD_DOCKER', None) == 'true':
    del os.link


try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from setuptools.command.test import test as TestCommand

def local(fname):
    return os.path.join(os.path.dirname(__file__), fname)

def read(fname):
    return open(local(fname)).read()

# On Python 3, we can't "from hamcrest import __version__" (get ImportError),
# so we extract the variable assignment and execute it ourselves.
fh = open(local('src/hamcrest/__init__.py'))
try:
    for line in fh:
        if re.match('__version__.*', line):
            exec(line)
finally:
    if fh:
        fh.close()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["tests"]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


test_dependencies = ['hypothesis>=1.11', 'pytest>=2.8', 'mock', 'pytest-cov']
try:
    from unittest import skipIf
except ImportError:
    test_dependencies.append('unittest2')


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
    install_requires=['setuptools', 'six'],
    tests_require=test_dependencies,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
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
