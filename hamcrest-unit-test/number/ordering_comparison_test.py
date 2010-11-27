__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.number.ordering_comparison import greater_than
from hamcrest.library.number.ordering_comparison import greater_than_or_equal_to
from hamcrest.library.number.ordering_comparison import less_than
from hamcrest.library.number.ordering_comparison import less_than_or_equal_to

from matcher_test import MatcherTest


class OrderingComparisonTest(MatcherTest):

    def testComparesObjectsForGreaterThan(self):
        assert_that(2, greater_than(1))
        assert_that(1, is_not(greater_than(1)))

    def testComparesObjectsForLessThan(self):
        assert_that(0, less_than(1))
        assert_that(1, is_not(less_than(1)))

    def testComparesObjectsForGreaterThanOrEqualTo(self):
        assert_that(2, greater_than_or_equal_to(1))
        assert_that(1, greater_than_or_equal_to(1))
        assert_that(0, is_not(greater_than_or_equal_to(1)))

    def testComparesObjectsForLessThanOrEqualTo(self):
        assert_that(0, less_than_or_equal_to(1))
        assert_that(1, less_than_or_equal_to(1))
        assert_that(2, is_not(less_than_or_equal_to(1)))

    def testHasAReadableDescription(self):
        self.assert_description('a value greater than <1>', greater_than(1))
        # Following test reveals typo in java hamcrest:
        self.assert_description('a value greater than or equal to <1>',
                                greater_than_or_equal_to(1))
        self.assert_description('a value less than <1>', less_than(1))
        # Reveals awkward wording that should be fixed:
        self.assert_description('a value equal to or less than <1>',
                                less_than_or_equal_to(1))


if __name__ == '__main__':
    unittest.main()
