__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnone import none, not_none
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class IsNoneTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsNone(self):
        ANY_NON_NULL_ARGUMENT = object()

        assert_that(None, none())
        assert_that(ANY_NON_NULL_ARGUMENT, is_not(none()))

        assert_that(ANY_NON_NULL_ARGUMENT, not_none())
        assert_that(None, is_not(not_none()))

    def testHasAReadableDescription(self):
        self.assert_description('None', none());
        self.assert_description('not None', not_none());


if __name__ == '__main__':
    unittest.main()
