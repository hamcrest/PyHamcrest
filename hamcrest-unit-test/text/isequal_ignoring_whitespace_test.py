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
from hamcrest.library.text.isequal_ignoring_whitespace import equal_to_ignoring_whitespace

from matcher_test import MatcherTest


matcher = equal_to_ignoring_whitespace('Hello World   how\n are we? ')

class IsEqualIgnoringWhiteSpaceTest(MatcherTest):

    def testPassesIfWordsAreSameButWhitespaceDiffers(self):
        assert_that('Hello World how are we?', matcher)
        assert_that('   Hello World   how are \n\n\twe?', matcher)

    def testFailsIfTextOtherThanWhitespaceDiffers(self):
        assert_that('Hello PLANET how are we?', is_not(matcher))
        assert_that('Hello World how are we', is_not(matcher))

    def testFailsIfWhitespaceIsAddedOrRemovedInMidWord(self):
        assert_that('HelloWorld how are we?', is_not(matcher))
        assert_that('Hello Wo rld how are we?', is_not(matcher))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, equal_to_ignoring_whitespace, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), is_not(matcher))

    def testDescribesItselfAsIgnoringWhiteSpace(self):
        self.assert_description("equal_to_ignoring_whitespace('Hello World   how\\n are we? ')",
                                matcher)

    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        assert_that(u'foo bar', equal_to_ignoring_whitespace(u'foo\n  bar'))

    def testCanApplyPlainStringToUnicodeMatcher(self):
        assert_that('foo bar', equal_to_ignoring_whitespace(u'foo\n  bar'))

    def testCanApplyUnicodeStringToPlainMatcher(self):
        assert_that(u'foo bar', equal_to_ignoring_whitespace('foo\n  bar'))


if __name__ == '__main__':
    unittest.main()
