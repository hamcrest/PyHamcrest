import sys

if __name__ == '__main__':
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.core.core.isinstanceof import *

from hamcrest_unit_test.matcher_test import MatcherTest

try:
    import unittest2 as unittest
except ImportError:
    import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsInstanceOfTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsInstanceOfASpecificClass(self):
        self.assert_matches('same class', instance_of(int), 1)

        self.assert_does_not_match('different class', instance_of(int), 'hi')
        self.assert_does_not_match('None', instance_of(int), None)

    def testMatcherCreationRequiresType(self):
        self.assertRaises(TypeError, instance_of, 'not a type')

    def testHasAReadableDescription(self):
        self.assert_description('an instance of int', instance_of(int));

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(instance_of(int), 3)

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", instance_of(int), 'bad')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", instance_of(int), 'bad')


if sys.version_info < (3,):
    class Parent():
        pass

    class Child(Parent):
        pass

class OldStyleIsInstanceTest(MatcherTest):

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testMatchesOldStyleClass(self):
        self.assert_matches('same class', instance_of(Parent), Parent())

        self.assert_does_not_match('different class', instance_of(Parent), 'not a Parent')
        self.assert_does_not_match('None', instance_of(Parent), None)

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testMatchesOldStyleSubclass(self):
        self.assert_matches('same class', instance_of(Parent), Child())

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testHasAReadableDescription(self):
        self.assert_description('an instance of Parent', instance_of(Parent));

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(instance_of(Parent), Parent())

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", instance_of(Parent), 'bad')

    @unittest.skipIf(sys.version_info >= (3,), "Old-style classes are not relevant under Python3+")
    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", instance_of(Parent), 'bad')

if __name__ == '__main__':
    unittest.main()
