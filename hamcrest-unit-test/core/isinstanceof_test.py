if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isinstanceof import instanceof
from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class IsInstanceOfTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsInstanceOfASpecificClass(self):
        assert_that(1, instanceof(int))
        assert_that(None, not_(instanceof(int)))
        assert_that('hello', not_(instanceof(int)))
    
    def testHasAReadableDescription(self):
        self.assert_description('an instance of int', instanceof(int));
    
    def testConstructorRequiresType(self):
        self.assertRaises(TypeError, instanceof, 3)
        

if __name__ == '__main__':
    unittest.main()
