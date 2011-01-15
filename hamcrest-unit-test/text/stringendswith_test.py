__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isnot import is_not
from hamcrest.library.text.stringendswith import ends_with

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringendswith = ends_with(EXCERPT)

class StringEndsWithTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assertTrue(not stringendswith.matches(EXCERPT + 'END'),
                    'should be false if excerpt at beginning')
        self.assertTrue(stringendswith.matches('START' + EXCERPT),
                    'should be true if excerpt at end')
        self.assertTrue(not stringendswith.matches('START' + EXCERPT + 'END'),
                    'should be false if excerpt in middle')
        self.assertTrue(stringendswith.matches(EXCERPT + EXCERPT),
                    'should be true if excerpt is repeated')

        self.assertTrue(not stringendswith.matches('Something else'),
                    'should be false if excerpt is not in string')
        self.assertTrue(not stringendswith.matches(EXCERPT[:-2]),
                    'should false if part of excerpt is at end of string')

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assertTrue(stringendswith.matches(EXCERPT),
                    'should be true if excerpt is entire string')

    def testHasAReadableDescription(self):
        self.assert_description("a string ending with 'a'", ends_with('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, ends_with, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), is_not(stringendswith))

    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        assert_that(u'foo bar baz', ends_with(u'baz'))

    def testCanApplyPlainStringToUnicodeMatcher(self):
        assert_that('foo bar baz', ends_with(u'baz'))

    def testCanApplyUnicodeStringToPlainMatcher(self):
        assert_that(u'foo bar baz', ends_with('baz'))


if __name__ == '__main__':
    unittest.main()
