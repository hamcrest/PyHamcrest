import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
from hamcrest_unit_test.matcher_test import MatcherTest

from .quasisequence import QuasiSequence
from .sequencemixin import GeneratorForm, SequenceForm

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceContainingInAnyOrderBase(object):
    def testMatchingSingleItemSequence(self):
        self.assert_matches(
            "Single item sequence", contains_inanyorder(equal_to(1)), self._sequence(1)
        )

    def testMatchesSequenceInOrder(self):
        self.assert_matches(
            "In order", contains_inanyorder(equal_to(1), equal_to(2)), self._sequence(1, 2)
        )

    def testMatchesSequenceOutOfOrder(self):
        self.assert_matches(
            "Out of order", contains_inanyorder(equal_to(1), equal_to(2)), self._sequence(2, 1)
        )

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches(
            "Values automatically wrapped with equal_to",
            contains_inanyorder(1, 2),
            self._sequence(2, 1),
        )

    def testDoesNotMatchEmptySequence(self):
        self.assert_mismatch_description(
            "no item matches: <1>, <2> in []", contains_inanyorder(1, 2), self._sequence()
        )

    def testEmptySequenceMatchesEmptySequence(self):
        self.assert_matches("Empty sequence", contains_inanyorder(), self._sequence())

    def testDoesNotMatchIfOneOfMultipleItemsMismatch(self):
        self.assert_mismatch_description(
            "not matched: <4>", contains_inanyorder(1, 2, 3), self._sequence(1, 2, 4)
        )

    def testDoesNotMatchWithMoreElementsThanExpected(self):
        self.assert_mismatch_description(
            "not matched: <2>", contains_inanyorder(1, 3), self._sequence(1, 2, 3)
        )

    def testDoesNotMatchWithFewerElementsThanExpected(self):
        self.assert_mismatch_description(
            "no item matches: <4> in [<1>, <2>, <3>]",
            contains_inanyorder(1, 2, 3, 4),
            self._sequence(1, 2, 3),
        )

    def testMatchesAnyConformingSequence(self):
        self.assert_matches("quasi-sequence", contains_inanyorder(1, 2), QuasiSequence())
        self.assert_does_not_match("non-sequence", contains_inanyorder(1, 2), object())

    def testHasAReadableDescription(self):
        self.assert_description(
            "a sequence over [<1>, <2>] in any order", contains_inanyorder(1, 2)
        )

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
            "not matched: <3>", contains_inanyorder(1, 2), self._sequence(1, 3)
        )

    def testDescribeMismatchOfNonSequence(self):
        self.assert_describe_mismatch("was <3>", contains_inanyorder(1, 2), 3)

    def testDescribeMismatchAfterMatch(self):
        matcher = contains_inanyorder(1, 2, 3)
        matcher.matches(self._sequence(3, 1))
        self.assert_describe_mismatch(
            "no item matches: <2> in [<3>, <1>]", matcher, self._sequence(3, 1)
        )


class IsConcreteSequenceContainingInAnyOrderTest(
    MatcherTest, IsSequenceContainingInAnyOrderBase, SequenceForm
):
    pass


class IsGeneratorSequenceContainingInAnyOrderTest(
    MatcherTest, IsSequenceContainingInAnyOrderBase, GeneratorForm
):
    pass


if __name__ == "__main__":
    unittest.main()
