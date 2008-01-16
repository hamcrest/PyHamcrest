if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.stringendswith import endswith

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringendswith = endswith(EXCERPT)

class StringEndsWithTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assert_(not stringendswith.matches(EXCERPT + 'END'),
                    'should be false if excerpt at beginning')
        self.assert_(stringendswith.matches('START' + EXCERPT),
                    'should be true if excerpt at end')
        self.assert_(not stringendswith.matches('START' + EXCERPT + 'END'),
                    'should be false if excerpt in middle')
        self.assert_(stringendswith.matches(EXCERPT + EXCERPT),
                    'should be true if excerpt is repeated')

        self.assert_(not stringendswith.matches('Something else'),
                    'should be false if excerpt is not in string')
        self.assert_(not stringendswith.matches(EXCERPT[:-2]),
                    'should false if part of excerpt is at end of string')

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assert_(stringendswith.matches(EXCERPT),
                    'should be true if excerpt is entire string')

    def testHasAReadableDescription(self):
        self.assert_description("a string ending with 'a'", endswith('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, endswith, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), not_(stringendswith))


if __name__ == '__main__':
    unittest.main()
