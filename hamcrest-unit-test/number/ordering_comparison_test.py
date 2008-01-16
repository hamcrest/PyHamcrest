if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.number.ordering_comparison import greaterthan
from hamcrest.library.number.ordering_comparison import greaterthan_or_equalto
from hamcrest.library.number.ordering_comparison import lessthan
from hamcrest.library.number.ordering_comparison import lessthan_or_equalto

from matcher_test import MatcherTest


class OrderingComparisonTest(MatcherTest):

    def testComparesObjectsForGreaterThan(self):
        assert_that(2, greaterthan(1))
        assert_that(1, not_(greaterthan(1)))

    def testComparesObjectsForLessThan(self):
        assert_that(0, lessthan(1))
        assert_that(1, not_(lessthan(1)))

    def testComparesObjectsForGreaterThanOrEqualTo(self):
        assert_that(2, greaterthan_or_equalto(1))
        assert_that(1, greaterthan_or_equalto(1))
        assert_that(0, not_(greaterthan_or_equalto(1)))

    def testComparesObjectsForLessThanOrEqualTo(self):
        assert_that(0, lessthan_or_equalto(1))
        assert_that(1, lessthan_or_equalto(1))
        assert_that(2, not_(lessthan_or_equalto(1)))
    
    def testHasAReadableDescription(self):
        self.assert_description('a value greater than <1>', greaterthan(1))
        # Following test reveals typo in java hamcrest:
        self.assert_description('a value greater than or equal to <1>',
                                greaterthan_or_equalto(1))
        self.assert_description('a value less than <1>', lessthan(1))
        # Reveals awkward wording that should be fixed:
        self.assert_description('a value equal to or less than <1>',
                                lessthan_or_equalto(1))


if __name__ == '__main__':
    unittest.main()
