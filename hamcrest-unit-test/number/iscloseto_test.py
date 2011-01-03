__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.library.number.iscloseto import close_to

from matcher_test import MatcherTest


class IsCloseToTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsEqualToAValueWithinSomeError(self):
        p = close_to(1.0, 0.5)

        self.assert_(p.matches(1.0))
        self.assert_(p.matches(0.5))
        self.assert_(p.matches(1.5))

        self.assert_(not p.matches(2.0), 'number too large')
        self.assert_(not p.matches(0.0), 'number too small')

    def testHasAReadableDescription(self):
        self.assert_description('a numeric value within <0.5> of <1.0>',
                                close_to(1.0, 0.5))

    def testConstructorRequiresNumbers(self):
        self.assertRaises(TypeError, close_to, 'a', 0.5)
        self.assertRaises(TypeError, close_to, 1.0, 'a')

    def testConstructorAcceptsOtherNumericTypes(self):
        close_to(5, 1)
        close_to(5L, 1L)

    def testFailsIfMatchingAgainstNonNumber(self):
        p = close_to(1.0, 0.5)

        self.assert_(not p.matches('a'), 'not a number')


if __name__ == '__main__':
    unittest.main()
