__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.anyof import any_of
from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.isnot import is_not

from matcher_test import MatcherTest


class AllOfTest(MatcherTest):

    def testEvaluatesToTheTheLogicalDisjunctionOfTwoOtherMatchers(self):
        assert_that('good', any_of(equal_to('good'), equal_to('good')))
        assert_that('good', any_of(equal_to('bad'), equal_to('good')))
        assert_that('good', any_of(equal_to('good'), equal_to('bad')))

        assert_that('good', is_not(any_of(equal_to('bad'), equal_to('bad'))))

    def testEvaluatesToTheTheLogicalDisjunctionOfManyOtherMatchers(self):
        assert_that('good', any_of(
                                equal_to('bad'),
                                equal_to('good'),
                                equal_to('bad'),
                                equal_to('bad'),
                                equal_to('bad')))
        assert_that('good', is_not(any_of(
                                equal_to('bad'),
                                equal_to('bad'),
                                equal_to('bad'),
                                equal_to('bad'),
                                equal_to('bad'))))

    def testHasAReadableDescription(self):
        self.assert_description("('good' or 'bad' or 'ugly')",
                    any_of(equal_to('good'), equal_to('bad'), equal_to('ugly')))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(
                                any_of(equal_to('good'), equal_to('bad')),
                                'good')

    def testMismatchDescriptionDescribesFirstFailingMatch(self):
        self.assert_mismatch_description(
                                "was 'ugly'",
                                any_of(equal_to('bad'), equal_to('good')),
                                'ugly')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
                                "was 'ugly'",
                                any_of(equal_to('bad'), equal_to('good')),
                                'ugly')


if __name__ == '__main__':
    unittest.main()
