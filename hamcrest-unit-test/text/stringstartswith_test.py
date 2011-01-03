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
from hamcrest.library.text.stringstartswith import starts_with

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringstartswith = starts_with(EXCERPT)

class StringStartsWithTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assert_(stringstartswith.matches(EXCERPT + 'END'),
                    'should be true if excerpt at beginning')
        self.assert_(not stringstartswith.matches('START' + EXCERPT),
                    'should be false if excerpt at end')
        self.assert_(not stringstartswith.matches('START' + EXCERPT + 'END'),
                    'should be false if excerpt in middle')
        self.assert_(stringstartswith.matches(EXCERPT + EXCERPT),
                    'should be true if excerpt is at beginning and repeated')

        self.assert_(not stringstartswith.matches('Something else'),
                    'should be false if excerpt is not in string')
        self.assert_(not stringstartswith.matches(EXCERPT[1:]),
                    'should false if part of excerpt is at start of string')

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assert_(stringstartswith.matches(EXCERPT),
                    'should be true if excerpt is entire string')

    def testHasAReadableDescription(self):
        self.assert_description("a string starting with 'a'", starts_with('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, starts_with, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), is_not(stringstartswith))

    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        assert_that(u'foo bar baz', starts_with(u'foo'))

    def testCanApplyPlainStringToUnicodeMatcher(self):
        assert_that('foo bar baz', starts_with(u'foo'))

    def testCanApplyUnicodeStringToPlainMatcher(self):
        assert_that(u'foo bar baz', starts_with('foo'))


if __name__ == '__main__':
    unittest.main()
