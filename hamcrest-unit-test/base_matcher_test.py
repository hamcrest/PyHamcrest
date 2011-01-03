__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

import unittest

from hamcrest.core.base_matcher import *


class TestingBaseMatcher(BaseMatcher):

    def describe_to(self, description):
        description.append_text('SOME DESCRIPTION')


class BaseMatcherTest(unittest.TestCase):

    def testDescribesItselfWithStrFunction(self):
        matcher = TestingBaseMatcher()
        self.assertEquals('SOME DESCRIPTION', str(matcher))


if __name__ == "__main__":
    unittest.main()
