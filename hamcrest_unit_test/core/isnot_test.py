if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.core.core.isnot import *

from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsNotTest(MatcherTest):

    def testEvaluatesToTheTheLogicalNegationOfAnotherMatcher(self):
        self.assert_matches('invert mismatch', is_not(equal_to('A')), 'B')
        self.assert_does_not_match('invert match', is_not(equal_to('A')), 'A')

    def testProvidesConvenientShortcutForNotEqualTo(self):
        self.assert_matches('invert mismatch', is_not('A'), 'B');
        self.assert_does_not_match('invert match', is_not('A'), 'A');

    def testHasAReadableDescription(self):
        self.assert_description("not 'A'", is_not('A'));

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(is_not('A'), 'B')

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'A'", is_not('A'), 'A')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'A'", is_not('A'), 'A')


if __name__ == '__main__':
    unittest.main()
