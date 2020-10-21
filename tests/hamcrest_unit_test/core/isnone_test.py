if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isnone import none, not_none
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsNoneTest(MatcherTest):
    def testEvaluatesToTrueIfArgumentIsNone(self):
        self.assert_matches("None", none(), None)

    def testEvaluatesToFalseIfArgumentIsNotNone(self):
        self.assert_does_not_match("not None", none(), object())

    def testHasAReadableDescription(self):
        self.assert_description("None", none())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(none(), None)

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", none(), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", none(), "bad")


class NotNoneTest(MatcherTest):
    def testEvaluatesToTrueIfArgumentIsNotNone(self):
        self.assert_matches("not None", not_none(), object())

    def testEvaluatesToFalseIfArgumentIsNone(self):
        self.assert_does_not_match("None", not_none(), None)

    def testHasAReadableDescription(self):
        self.assert_description("not None", not_none())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(not_none(), "hi")

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("but was <None>", not_none(), None)

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("but was <None>", not_none(), None)


if __name__ == "__main__":
    unittest.main()
