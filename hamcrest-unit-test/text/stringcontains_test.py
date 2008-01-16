if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.stringcontains import containsstring

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringcontains = containsstring(EXCERPT)

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
        self.assert_description("a string containing 'a'", containsstring('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, containsstring, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), not_(stringcontains))


if __name__ == '__main__':
    unittest.main()
