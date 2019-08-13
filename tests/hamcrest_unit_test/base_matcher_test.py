if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")

import unittest

from hamcrest.core.base_matcher import *

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class TestingBaseMatcher(BaseMatcher):
    def describe_to(self, description):
        description.append_text("SOME DESCRIPTION")


class BaseMatcherTest(unittest.TestCase):
    def testStrFunctionShouldDescribeMatcher(self):
        matcher = TestingBaseMatcher()
        self.assertEqual("SOME DESCRIPTION", str(matcher))


if __name__ == "__main__":
    unittest.main()
