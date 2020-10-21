import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containingvalue import has_value
from hamcrest_unit_test.matcher_test import MatcherTest

from .quasidict import QuasiDictionary

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingValueTest(MatcherTest):
    def testMatchesSingletonDictionaryContainingValue(self):
        dict = {"a": 1}
        self.assert_matches("same single value", has_value(equal_to(1)), dict)

    def testMatchesDictionaryContainingValue(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("Matches 1", has_value(equal_to(1)), dict)
        self.assert_matches("Matches 3", has_value(equal_to(3)), dict)

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("Matches 3", has_value(3), dict)

    def testDoesNotMatchEmptyDictionary(self):
        self.assert_does_not_match("empty", has_value(1), {})

    def testDoesNotMatchDictionaryMissingValue(self):
        dict = {"a": 1, "b": 2, "c": 3}
        self.assert_does_not_match("no matching value", has_value(4), dict)

    def testMatchesAnyConformingDictionary(self):
        self.assert_matches("quasi-dictionary", has_value("1"), QuasiDictionary())
        self.assert_does_not_match("non-dictionary", has_value("1"), object())

    def testHasReadableDescription(self):
        self.assert_description("a dictionary containing value 'a'", has_value("a"))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_value(1), {"a": 1})

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", has_value(1), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", has_value(1), "bad")


if __name__ == "__main__":
    unittest.main()
