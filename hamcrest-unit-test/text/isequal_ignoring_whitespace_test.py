if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.isequal_ignoring_whitespace import equalto_ignoring_whitespace

from matcher_test import MatcherTest


matcher = equalto_ignoring_whitespace('Hello World   how\n are we? ')

class IsEqualIgnoringWhiteSpaceTest(MatcherTest):

    def testPassesIfWordsAreSameButWhitespaceDiffers(self):
        assert_that('Hello World how are we?', matcher)
        assert_that('   Hello World   how are \n\n\twe?', matcher)

    def testFailsIfTextOtherThanWhitespaceDiffers(self):
        assert_that('Hello PLANET how are we?', not_(matcher))
        assert_that('Hello World how are we', not_(matcher))

    def testFailsIfWhitespaceIsAddedOrRemovedInMidWord(self):
        assert_that('HelloWorld how are we?', not_(matcher))
        assert_that('Hello Wo rld how are we?', not_(matcher))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, equalto_ignoring_whitespace, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), not_(matcher))


if __name__ == '__main__':
    unittest.main()
