if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.anyof import anyof
from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class AllOfTest(MatcherTest):

    def testEvaluatesToTheTheLogicalDisjunctionOfTwoOtherMatchers(self):
        assert_that('good', anyof(equalto('good'), equalto('good')))
        assert_that('good', anyof(equalto('bad'), equalto('good')))
        assert_that('good', anyof(equalto('good'), equalto('bad')))
        
        assert_that('good', not_(anyof(equalto('bad'), equalto('bad'))))

    def testEvaluatesToTheTheLogicalDisjunctionOfManyOtherMatchers(self):
        assert_that('good', anyof(
                                equalto('bad'),
                                equalto('good'),
                                equalto('bad'),
                                equalto('bad'),
                                equalto('bad')))
        assert_that('good', not_(anyof(
                                equalto('bad'),
                                equalto('bad'),
                                equalto('bad'),
                                equalto('bad'),
                                equalto('bad'))))

    def testHasAReadableDescription(self):
        self.assert_description("('good' or 'bad' or 'ugly')",
                    anyof(equalto('good'), equalto('bad'), equalto('ugly')))


if __name__ == '__main__':
    unittest.main()
