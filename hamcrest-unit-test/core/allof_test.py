if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.allof import allof
from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class AllOfTest(MatcherTest):

    def testEvaluatesToTheTheLogicalConjunctionOfTwoOtherMatchers(self):
        assert_that('good', allof(equalto('good'), equalto('good')))
        
        assert_that('good', not_(allof(equalto('bad'), equalto('good'))))
        assert_that('good', not_(allof(equalto('good'), equalto('bad'))))
        assert_that('good', not_(allof(equalto('bad'), equalto('bad'))))

    def testEvaluatesToTheTheLogicalConjunctionOfManyOtherMatchers(self):
        assert_that('good', allof(
                                equalto('good'),
                                equalto('good'),
                                equalto('good'),
                                equalto('good'),
                                equalto('good')))
        assert_that('good', not_(allof(
                                equalto('good'),
                                equalto('good'),
                                equalto('bad'),
                                equalto('good'),
                                equalto('good'))))

    def testHasAReadableDescription(self):
        self.assert_description("('good' and 'bad' and 'ugly')",
                    allof(equalto('good'), equalto('bad'), equalto('ugly')))


if __name__ == '__main__':
    unittest.main()
