__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.number.iscloseto import *

from matcher_test import MatcherTest
import unittest


class IsCloseToTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsEqualToAValueWithinSomeError(self):
        matcher = close_to(1.0, 0.5)

        self.assert_matches('equal', matcher, 1.0)
        self.assert_matches('less but within delta', matcher, 0.5)
        self.assert_matches('greater but within delta', matcher, 1.5)

        self.assert_does_not_match('too small', matcher, 0.4)
        self.assert_does_not_match('too large', matcher, 1.6)

    def testMatcherCreationAcceptsOtherNumericTypes(self):
        close_to(5, 1)
        close_to(5L, 1L)

    def testMatcherCreationRequiresNumbers(self):
        self.assertRaises(TypeError, close_to, 'a', 0.5)
        self.assertRaises(TypeError, close_to, 1.0, 'a')

    def testFailsIfMatchingAgainstNonNumber(self):
        self.assert_does_not_match('not a number', close_to(1.0, 0.5), 'a')

    def testHasAReadableDescription(self):
        self.assert_description('a numeric value within <0.5> of <1.0>',
                                close_to(1.0, 0.5))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(close_to(1.0, 0.5), 1.0)

    def testMismatchDescriptionShowsActualDeltaIfArgumentIsNumeric(self):
        self.assert_mismatch_description('<1.7> differed by <0.7>',
                                         close_to(1.0, 0.5), 1.7)

    def testMismatchDescriptionShowsActualArgumentIfNotNumeric(self):
        self.assert_mismatch_description("was 'bad'", close_to(1.0, 0.5), 'bad')

    def testDescribeMismatchShowsActualDeltaIfArgumentIsNumeric(self):
        self.assert_describe_mismatch('<1.7> differed by <0.7>',
                                      close_to(1.0, 0.5), 1.7)

    def testDescribeMismatchShowsActualArgumentIfNotNumeric(self):
        self.assert_describe_mismatch("was 'bad'", close_to(1.0, 0.5), 'bad')


if __name__ == '__main__':
    unittest.main()
