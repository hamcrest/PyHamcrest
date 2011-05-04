if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.text.isequal_ignoring_whitespace import *

from hamcrest_unit_test.matcher_test import MatcherTest
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


matcher = equal_to_ignoring_whitespace('Hello World   how\n are we? ')

class IsEqualIgnoringWhiteSpaceTest(MatcherTest):

    def testPassesIfWordsAreSameButWhitespaceDiffers(self):
        self.assert_matches('less whitespace',
                            matcher, 'Hello World how are we?')
        self.assert_matches('more whitespace',
                            matcher, '   Hello World   how are \n\n\twe?')

    def testFailsIfTextOtherThanWhitespaceDiffers(self):
        self.assert_does_not_match('wrong word',
                                   matcher, 'Hello PLANET how are we?')
        self.assert_does_not_match('incomplete',
                                   matcher, 'Hello World how are we')

    def testFailsIfWhitespaceIsAddedOrRemovedInMidWord(self):
        self.assert_does_not_match('need whitespace between Hello and World',
                                   matcher, 'HelloWorld how are we?')
        self.assert_does_not_match('wrong whitespace within World',
                                   matcher, 'Hello Wo rld how are we?')

    def testMatcherCreationRequiresString(self):
        self.assertRaises(TypeError, equal_to_ignoring_whitespace, 3)

    def testFailsIfMatchingAgainstNonString(self):
        self.assert_does_not_match('non-string', matcher, object())

    def testCanApplyUnicodeStringToUnicodeMatcher(self):
        self.assert_matches('unicode-unicode',
                            equal_to_ignoring_whitespace(u'foo\nbar'),
                            u'foo bar')

    def testCanApplyPlainStringToUnicodeMatcher(self):
        self.assert_matches('unicode-ascii',
                            equal_to_ignoring_whitespace(u'foo\nbar'),
                            'foo bar')

    def testCanApplyUnicodeStringToPlainMatcher(self):
        self.assert_matches('ascii-unicode',
                            equal_to_ignoring_whitespace('foo\n bar'),
                            u'foo bar')

    def testDescribesItselfAsIgnoringWhiteSpace(self):
        self.assert_description("'foo\\nbar' ignoring whitespace",
                                equal_to_ignoring_whitespace('foo\nbar'))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(
                        equal_to_ignoring_whitespace('foo\nbar'), 'foo bar')

    def testMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", matcher, 'bad')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", matcher, 'bad')


if __name__ == '__main__':
    unittest.main()
