import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containingkey import has_key
from hamcrest_unit_test.matcher_test import MatcherTest

from .quasidict import QuasiDictionary

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingKeyTest(MatcherTest):
    def testMatchesSingletonDictionaryContainingKey(self):
        dict = {"a": 1}
        self.assert_matches("same single key", has_key(equal_to("a")), dict)

    def testMatchesDictionaryContainingKey(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("Matches a", has_key(equal_to("a")), dict)
        self.assert_matches("Matches c", has_key(equal_to("c")), dict)

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("Matches c", has_key("c"), dict)

    def testDoesNotMatchEmptyDictionary(self):
        self.assert_does_not_match("empty", has_key("foo"), {})

    def testDoesNotMatchDictionaryMissingKey(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_does_not_match("no matching key", has_key("d"), dict)

    def testMatchesAnyConformingDictionary(self):
        self.assert_matches("quasi-dictionary", has_key(1), QuasiDictionary())
        self.assert_does_not_match("non-dictionary", has_key(1), object())

    def testHasReadableDescription(self):
        self.assert_description("a dictionary containing key 'a'", has_key("a"))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_key("a"), {"a": 1})

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", has_key("a"), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", has_key("a"), "bad")


if __name__ == "__main__":
    unittest.main()
