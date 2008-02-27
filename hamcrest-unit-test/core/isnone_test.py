if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnone import none, not_none
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


ANY_NON_NULL_ARGUMENT = object()

class IsNoneTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsNone(self):
        assert_that(None, none())
        assert_that(ANY_NON_NULL_ARGUMENT, is_not(none()))
        
        assert_that(ANY_NON_NULL_ARGUMENT, not_none())
        assert_that(None, is_not(not_none()))

    def testHasAReadableDescription(self):
        self.assert_description('None', none());
        self.assert_description('not None', not_none());
        

if __name__ == '__main__':
    unittest.main()
