__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

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

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(
                                all_of(equal_to('good'), equal_to('good')),
                                'good')

    def testMismatchDescriptionDescribesFirstFailingMatch(self):
        self.assert_mismatch_description(
                                "'good' was 'bad'",
                                all_of(equal_to('bad'), equal_to('good')),
                                'bad')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
                                "'good' was 'bad'",
                                all_of(equal_to('bad'), equal_to('good')),
                                'bad')


if __name__ == '__main__':
    unittest.main()
