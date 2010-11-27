__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isinstanceof import instance_of
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class IsInstanceOfTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsInstanceOfASpecificClass(self):
        assert_that(1, instance_of(int))
        assert_that(None, is_not(instance_of(int)))
        assert_that('hello', is_not(instance_of(int)))

    def testHasAReadableDescription(self):
        self.assert_description('an instance of int', instance_of(int));

    def testConstructorRequiresType(self):
        self.assertRaises(TypeError, instance_of, 3)


if __name__ == '__main__':
    unittest.main()
