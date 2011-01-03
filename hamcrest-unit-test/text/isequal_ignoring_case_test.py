__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.isequal_ignoring_case import equal_to_ignoring_case

from matcher_test import MatcherTest


matcher = equal_to_ignoring_case('heLLo')

class IsEqualIgnoringCaseTest(MatcherTest):

    def testIgnoresCaseOfCharsInString(self):
        assert_that('HELLO', matcher)
        assert_that('hello', matcher)
        assert_that('HelLo', matcher)

        assert_that('bye', is_not(matcher))

    def testFailsIfAdditionalWhitespaceIsPresent(self):
        assert_that('heLLo ', is_not(matcher))
        assert_that(' heLLo', is_not(matcher))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, equal_to_ignoring_case, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), is_not(matcher))

    def testDescribesItselfAsCaseInsensitive(self):
        self.assert_description("equal_to_ignoring_case('heLLo')", matcher)
    
    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        assert_that(u'HelLo', equal_to_ignoring_case(u'heLLo'))

    def testCanApplyPlainStringToUnicodeMatcher(self):
        assert_that('HelLo', equal_to_ignoring_case(u'heLLo'))

    def testCanApplyUnicodeStringToPlainMatcher(self):
        assert_that(u'HelLo', equal_to_ignoring_case('heLLo'))


if __name__ == '__main__':
    unittest.main()
