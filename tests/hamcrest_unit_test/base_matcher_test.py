if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")

import unittest

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest_unit_test.matcher_test import assert_match_description, assert_mismatch_description

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class FailingBaseMatcher(BaseMatcher):
    def describe_to(self, description):
        description.append_text("SOME DESCRIPTION")

    def _matches(self, item):
        return False


class PassingBaseMatcher(BaseMatcher):
    def _matches(self, item):
        return True


class BaseMatcherTest(unittest.TestCase):
    def testStrFunctionShouldDescribeMatcher(self):
        matcher = FailingBaseMatcher()
        self.assertEqual("SOME DESCRIPTION", str(matcher))

    def testMismatchDescriptionShouldDescribeItem(self):
        assert_mismatch_description("was <99>", FailingBaseMatcher(), 99)

    def testMatchDescriptionShouldDescribeItem(self):
        assert_match_description("was <99>", PassingBaseMatcher(), 99)

    def testMatcherReprShouldDescribeMatcher(self):
        assert repr(FailingBaseMatcher()) == "<FailingBaseMatcher(SOME DESCRIPTION)>"

    def testMatcherReprShouldTruncateLongDescription(self):
        class LongDescriptionMatcher(BaseMatcher):
            def describe_to(self, description):
                description.append_text("1234 " * 13)

        assert (
            repr(LongDescriptionMatcher())
            == "<LongDescriptionMatcher(1234 1234 1234 1234 1234 1234 1234 1234 1234 1234 1234...)>"
        )


if __name__ == "__main__":
    unittest.main()
