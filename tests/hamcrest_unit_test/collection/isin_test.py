import unittest

from hamcrest.library.collection.isin import is_in
from hamcrest_unit_test.matcher_test import MatcherTest

from .sequencemixin import GeneratorForm, SequenceForm

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


sequence = ("a", "b", "c")


class IsInTestBase(object):
    def testReturnsTrueIfArgumentIsInSequence(self):
        matcher = is_in(self._sequence(*sequence))

        self.assert_matches("has a", matcher, "a")
        self.assert_matches("has b", matcher, "b")
        self.assert_matches("has c", matcher, "c")
        self.assert_does_not_match("no d", matcher, "d")

    def testHasReadableDescription(self):
        self.assert_description("one of ('a', 'b', 'c')", is_in(self._sequence(*sequence)))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(is_in(self._sequence(*sequence)), "a")

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", is_in(self._sequence(*sequence)), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", is_in(self._sequence(*sequence)), "bad")


class IsInConcreteSequenceTest(MatcherTest, IsInTestBase, SequenceForm):
    pass


class IsInGeneratorTest(MatcherTest, IsInTestBase, GeneratorForm):
    pass


if __name__ == "__main__":
    unittest.main()
