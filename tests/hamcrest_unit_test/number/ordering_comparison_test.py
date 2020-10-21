if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest
from datetime import date

from hamcrest.library.number.ordering_comparison import (
    greater_than,
    greater_than_or_equal_to,
    less_than,
    less_than_or_equal_to,
)
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class OrderingComparisonTest(MatcherTest):
    def testComparesObjectsForGreaterThan(self):
        self.assert_matches("match", greater_than(1), 2)
        self.assert_does_not_match("no match", greater_than(1), 1)

    def testComparesObjectsForLessThan(self):
        self.assert_matches("match", less_than(1), 0)
        self.assert_does_not_match("no match", less_than(1), 1)

    def testComparesObjectsForGreaterThanOrEqualTo(self):
        self.assert_matches("match", greater_than_or_equal_to(1), 2)
        self.assert_matches("match", greater_than_or_equal_to(1), 1)
        self.assert_does_not_match("no match", greater_than_or_equal_to(1), 0)

    def testComparesObjectsForLessThanOrEqualTo(self):
        self.assert_matches("match", less_than_or_equal_to(1), 0)
        self.assert_matches("match", less_than_or_equal_to(1), 1)
        self.assert_does_not_match("no match", less_than_or_equal_to(1), 2)

    def testSupportsDifferentTypesOfComparableObjects(self):
        self.assert_matches("strings", greater_than("bb"), "cc")
        self.assert_matches("dates", less_than(date.today()), date.min)

    def testHasAReadableDescription(self):
        self.assert_description("a value greater than <1>", greater_than(1))
        self.assert_description("a value greater than or equal to <1>", greater_than_or_equal_to(1))
        self.assert_description("a value less than <1>", less_than(1))
        self.assert_description("a value less than or equal to <1>", less_than_or_equal_to(1))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(greater_than(1), 2)
        self.assert_no_mismatch_description(less_than(1), 0)
        self.assert_no_mismatch_description(greater_than_or_equal_to(1), 1)
        self.assert_no_mismatch_description(less_than_or_equal_to(1), 1)

    def testMismatchDescription(self):
        self.assert_mismatch_description("was <0>", greater_than(1), 0)
        self.assert_mismatch_description("was <2>", less_than(1), 2)
        self.assert_mismatch_description("was <0>", greater_than_or_equal_to(1), 0)
        self.assert_mismatch_description("was <2>", less_than_or_equal_to(1), 2)

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was <0>", greater_than(1), 0)
        self.assert_describe_mismatch("was <2>", less_than(1), 2)
        self.assert_describe_mismatch("was <0>", greater_than_or_equal_to(1), 0)
        self.assert_describe_mismatch("was <2>", less_than_or_equal_to(1), 2)


if __name__ == "__main__":
    unittest.main()
