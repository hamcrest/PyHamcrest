import sys
import unittest

from hamcrest.core.core.isinstanceof import instance_of
from hamcrest_unit_test.matcher_test import MatcherTest

if __name__ == "__main__":
    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")


__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsInstanceOfTest(MatcherTest):
    def testEvaluatesToTrueIfArgumentIsInstanceOfASpecificClass(self):
        self.assert_matches("same class", instance_of(int), 1)

        self.assert_does_not_match("different class", instance_of(int), "hi")
        self.assert_does_not_match("None", instance_of(int), None)

    def testMatcherCreationRequiresType(self):
        self.assertRaises(TypeError, instance_of, "not a type")

    def testHasAReadableDescription(self):
        self.assert_description("an instance of int", instance_of(int))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(instance_of(int), 3)

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", instance_of(int), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", instance_of(int), "bad")


if __name__ == "__main__":
    unittest.main()
