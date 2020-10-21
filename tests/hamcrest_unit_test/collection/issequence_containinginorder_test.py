import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.issequence_containinginorder import contains, contains_exactly
from hamcrest_unit_test.matcher_test import MatcherTest

from .quasisequence import QuasiSequence
from .sequencemixin import GeneratorForm, SequenceForm

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceContainingInOrderTestBase(object):
    def testMatchingSingleItemSequence(self):
        self.assert_matches(
            "Single item sequence", contains_exactly(equal_to(1)), self._sequence(1)
        )

    def testMatchingMultipleItemSequence(self):
        self.assert_matches(
            "Multiple item sequence",
            contains_exactly(equal_to(1), equal_to(2), equal_to(3)),
            self._sequence(1, 2, 3),
        )

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches(
            "Values automatically wrapped with equal_to",
            contains_exactly(1, 2, 3),
            self._sequence(1, 2, 3),
        )

    def testDoesNotMatchWithMoreElementsThanExpected(self):
        self.assert_mismatch_description(
            "Not matched: <4>", contains_exactly(1, 2, 3), self._sequence(1, 2, 3, 4)
        )

    def testDoesNotMatchWithFewerElementsThanExpected(self):
        self.assert_mismatch_description(
            "No item matched: <3>", contains_exactly(1, 2, 3), self._sequence(1, 2)
        )

    def testDoesNotMatchIfSingleItemMismatches(self):
        self.assert_mismatch_description("item 0: was <3>", contains_exactly(4), self._sequence(3))

    def testDoesNotMatchIfOneOfMultipleItemsMismatch(self):
        self.assert_mismatch_description(
            "item 2: was <4>", contains_exactly(1, 2, 3), self._sequence(1, 2, 4)
        )

    def testDoesNotMatchEmptySequence(self):
        self.assert_mismatch_description(
            "No item matched: <4>", contains_exactly(4), self._sequence()
        )

    def testEmptySequenceMatchesEmptySequence(self):
        self.assert_matches("Empty sequence", contains_exactly(), self._sequence())

    def testMatchesAnyConformingSequence(self):
        self.assert_matches("quasi-sequence", contains_exactly(1, 2), QuasiSequence())
        self.assert_does_not_match("non-sequence", contains_exactly(1, 2), object())

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing [<1>, <2>]", contains_exactly(1, 2))

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
            "item 1: was <3>", contains_exactly(1, 2), self._sequence(1, 3)
        )

    def testDescribeMismatchOfNonSequence(self):
        self.assert_describe_mismatch("was <3>", contains_exactly(1, 2), 3)

    def testContainsDeprecated(self):
        self.assert_deprecated("deprecated - use contains_exactly(*items)", contains)


class IsConcreteSequenceContainingInOrderTest(
    MatcherTest, IsSequenceContainingInOrderTestBase, SequenceForm
):
    pass


class IsGeneratorSequenceContainingInOrderTest(
    MatcherTest, IsSequenceContainingInOrderTestBase, GeneratorForm
):
    pass


if __name__ == "__main__":
    unittest.main()
