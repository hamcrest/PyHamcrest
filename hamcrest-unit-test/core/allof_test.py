if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.allof import all_of
from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class AllOfTest(MatcherTest):

    def testEvaluatesToTheTheLogicalConjunctionOfTwoOtherMatchers(self):
        assert_that('good', all_of(equal_to('good'), equal_to('good')))
        
        assert_that('good', is_not(all_of(equal_to('bad'), equal_to('good'))))
        assert_that('good', is_not(all_of(equal_to('good'), equal_to('bad'))))
        assert_that('good', is_not(all_of(equal_to('bad'), equal_to('bad'))))

    def testEvaluatesToTheTheLogicalConjunctionOfManyOtherMatchers(self):
        assert_that('good', all_of(
                                equal_to('good'),
                                equal_to('good'),
                                equal_to('good'),
                                equal_to('good'),
                                equal_to('good')))
        assert_that('good', is_not(all_of(
                                equal_to('good'),
                                equal_to('good'),
                                equal_to('bad'),
                                equal_to('good'),
                                equal_to('good'))))

    def testHasAReadableDescription(self):
        self.assert_description("('good' and 'bad' and 'ugly')",
                    all_of(equal_to('good'), equal_to('bad'), equal_to('ugly')))


if __name__ == '__main__':
    unittest.main()
