import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.issequence_containing import has_item, has_items
from hamcrest_unit_test.matcher_test import MatcherTest

from .quasisequence import QuasiSequence
from .sequencemixin import GeneratorForm, SequenceForm

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceContainingTestBase(object):
    def testMatchesASequenceThatContainsAnElementMatchingTheGivenMatcher(self):
        self.assert_matches(
            "sequence contains 'a'", has_item(equal_to("a")), self._sequence("a", "b", "c")
        )

    def testNoMatchIfSequenceDoesntContainAnElementMatchingTheGivenMatcher(self):
        self.assert_does_not_match(
            "sequence without 'a'", has_item(equal_to("a")), self._sequence("b", "c")
        )
        self.assert_does_not_match("empty", has_item(equal_to("a")), [])

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches("sequence contains 'a'", has_item("a"), self._sequence("a", "b", "c"))
        self.assert_does_not_match("sequence without 'a'", has_item("a"), self._sequence("b", "c"))

    def testMatchesAnyConformingSequence(self):
        self.assert_matches("quasi-sequence", has_item(1), QuasiSequence())
        self.assert_does_not_match("non-sequence", has_item(1), object())

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing 'a'", has_item("a"))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_item("a"), self._sequence("a", "b"))

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was <42>", has_item("a"), 42)

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was <42>", has_item("a"), 42)


class IsConcreteSequenceContaining(MatcherTest, SequenceForm, IsSequenceContainingTestBase):
    pass


class IsGeneratorContaining(MatcherTest, GeneratorForm, IsSequenceContainingTestBase):
    pass


class IsSequenceContainingItemsTestBase(object):
    def testShouldMatchCollectionContainingAllItems(self):
        self.assert_matches(
            "contains all items",
            has_items(equal_to("a"), equal_to("b"), equal_to("c")),
            self._sequence("a", "b", "c"),
        )

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches(
            "Values automatically wrapped with equal_to",
            has_items("a", "b", "c"),
            self._sequence("a", "b", "c"),
        )

    def testShouldMatchCollectionContainingAllItemsInDifferentOrder(self):
        self.assert_matches(
            "all items in different order", has_items("a", "b", "c"), self._sequence("c", "b", "a")
        )

    def testShouldMatchCollectionContainingAllItemsPlusExtras(self):
        self.assert_matches(
            "all items plus extras",
            has_items("a", "b", "c"),
            self._sequence("e", "c", "b", "a", "d"),
        )

    def testNoMatchIfCollectionDoesntSatisfyAllMatchers(self):
        self.assert_does_not_match(
            "missing 'a'", has_items("a", "b", "c"), self._sequence("e", "c", "b", "d")
        )

    def testHasAReadableDescription(self):
        self.assert_description(
            "(a sequence containing 'a' and a sequence containing 'b')", has_items("a", "b")
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_items("a", "b"), self._sequence("a", "b"))

    def testMismatchDescriptionShowsFirstUnmetMatcherAndActualArgument(self):
        self.assert_mismatch_description(
            "a sequence containing 'a' was <42>", has_items("a", "b"), 42
        )

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("a sequence containing 'a' was <42>", has_items("a", "b"), 42)


class IsConcreteSequenceContainingItemsTest(
    MatcherTest, IsSequenceContainingItemsTestBase, SequenceForm
):
    pass


class IsGeneratorSequenceContainingItemsTest(
    MatcherTest, IsSequenceContainingItemsTestBase, GeneratorForm
):
    pass


if __name__ == "__main__":
    unittest.main()
