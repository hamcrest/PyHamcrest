__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.stringcontains import contains_string

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringcontains = contains_string(EXCERPT)

class StringContainsTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assert_(stringcontains.matches(EXCERPT + 'END'),
                    'should be true if excerpt at beginning')
        self.assert_(stringcontains.matches('START' + EXCERPT),
                    'should be true if excerpt at end')
        self.assert_(stringcontains.matches('START' + EXCERPT + 'END'),
                    'should be true if excerpt in middle')
        self.assert_(stringcontains.matches(EXCERPT + EXCERPT),
                    'should be true if excerpt is repeated')

        self.assert_(not stringcontains.matches('Something else'),
                    'should be false if excerpt is not in string')
        self.assert_(not stringcontains.matches(EXCERPT[1:]),
                    'should be false if part of excerpt is in string')

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assert_(stringcontains.matches(EXCERPT),
                    'should be true if excerpt is entire string')

    def testHasAReadableDescription(self):
        self.assert_description("a string containing 'a'", contains_string('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, contains_string, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), is_not(stringcontains))

    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        assert_that(u'foo bar baz', contains_string(u'bar'))

    def testCanApplyPlainStringToUnicodeMatcher(self):
        assert_that('foo bar baz', contains_string(u'bar'))

    def testCanApplyUnicodeStringToPlainMatcher(self):
        assert_that(u'foo bar baz', contains_string('bar'))


if __name__ == '__main__':
    unittest.main()
