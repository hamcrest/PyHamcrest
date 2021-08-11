import os
import re

from setuptools import find_packages, setup

# need to kill off link if we're in docker builds
if os.environ.get("PYTHON_BUILD_DOCKER", None) == "true":
    del os.link

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def read(fname):
    return open(fname).read()


# On Python 3, we can't "from hamcrest import __version__" (get ImportError),
# so we extract the variable assignment and execute it ourselves.
fh = open("src/hamcrest/__init__.py")

# this will be overridden
__version__ = None
try:
    for line in fh:
        if re.match("__version__.*", line):
            exec(line)

finally:
    if fh:
        fh.close()

assert __version__ is not None

REQUIREMENTS_DOCS = ["sphinx~=3.0", "alabaster~=0.7"]
TESTS_BASIC = [
    "pytest>=5.0",
    "pytest-sugar",
    "coverage",
    "pytest-mypy-plugins; python_version<'3.10'",
    "types-mock",
]
TESTS_NUMPY = ["numpy"]
DEV_TOOLS = [
    "towncrier",
    "twine",
    "pytest-xdist",
    "pytest-mypy",
    "flake8",
    "black",
    "tox",
    "tox-pyenv",
    "tox-asdf",
]


params = dict(
    name="PyHamcrest",
    version=__version__,  # flake8:noqa
    author="Chris Rose",
    author_email="offline@offby1.net",
    description="Hamcrest framework for matcher objects",
    license="New BSD",
    platforms=["All"],
    keywords="hamcrest matchers pyunit unit test testing unittest unittesting",
    url="https://github.com/hamcrest/PyHamcrest",
    download_url="http://pypi.python.org/packages/source/P/PyHamcrest/PyHamcrest-%s.tar.gz"
    % __version__,
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"hamcrest": ["py.typed"]},
    provides=["hamcrest"],
    long_description=read("README.rst"),
    python_requires=">=3.5",
    install_requires=[],
    extras_require={
        "docs": REQUIREMENTS_DOCS,
        "tests": TESTS_BASIC,
        "tests-numpy": TESTS_BASIC + TESTS_NUMPY,
        "dev": REQUIREMENTS_DOCS + TESTS_BASIC + DEV_TOOLS,
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
)

all_params = dict(params.items())
setup(**all_params)
