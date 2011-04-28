import os
import sys
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == "__main__":
    sys.path.insert(0, '..')


def alltests():
    """Returns suite of all tests in this directory and below."""
    testloader = unittest.defaultTestLoader
    suite = testloader.suiteClass()

    fullpath = os.path.abspath(os.path.dirname(sys.argv[0]))
    for dirpath, dirnames, filenames in os.walk(fullpath):
        sys.path.insert(0, dirpath)
        for file in filenames:
            if file.endswith('test.py'):
                (name, ext) = os.path.splitext(file)
                module = __import__(name)
                suite.addTest(testloader.loadTestsFromModule(module))
        sys.path.pop(0)

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='alltests')
