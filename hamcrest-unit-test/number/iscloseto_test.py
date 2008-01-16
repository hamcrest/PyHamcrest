if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.library.number.iscloseto import closeto

from matcher_test import MatcherTest


class IsCloseToTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsEqualToAValueWithinSomeError(self):
        p = closeto(1.0, 0.5)

        self.assert_(p.matches(1.0))
        self.assert_(p.matches(0.5))
        self.assert_(p.matches(1.5))

        self.assert_(not p.matches(2.0), 'number too large')
        self.assert_(not p.matches(0.0), 'number too small')
        self.assert_(not p.matches('a'), 'not a number')
    
    def testHasAReadableDescription(self):
        self.assert_description('a numeric value within <0.5> of <1.0>',
                                closeto(1.0, 0.5))

    def testConstructorRequiresNumbers(self):
        self.assertRaises(TypeError, closeto, 'a', 0.5)
        self.assertRaises(TypeError, closeto, 1.0, 'a')

    def testConstructorAcceptsOtherNumericTypes(self):
        closeto(5, 1)
        closeto(5L, 1L)

    def testFailsIfMatchingAgainstNonNumber(self):
        self.assert_(not closeto(1.0, 0.5).matches('a'), 'not a number')


if __name__ == '__main__':
    unittest.main()
