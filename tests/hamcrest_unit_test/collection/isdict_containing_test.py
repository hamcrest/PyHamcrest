import unittest

from hamcrest import starts_with
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containing import has_entry
from hamcrest_unit_test.matcher_test import (
    MatcherTest,
    assert_match_description,
    assert_mismatch_description,
)

from .quasidict import QuasiDictionary

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingTest(MatcherTest):
    def testMatchesDictionaryContainingMatchingKeyAndValue(self):
        dict = {"a": 1, "b": 2}
        self.assert_matches("has a:1", has_entry(equal_to("a"), equal_to(1)), dict)
        self.assert_matches("has b:2", has_entry(equal_to("b"), equal_to(2)), dict)
        self.assert_does_not_match("no c:3", has_entry(equal_to("c"), equal_to(3)), dict)

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        dict = {"a": 1, "b": 2}
        self.assert_matches("has a:1", has_entry("a", equal_to(1)), dict)
        self.assert_matches("has b:2", has_entry(equal_to("b"), 2), dict)
        self.assert_does_not_match("no c:3", has_entry("c", 3), dict)

    def testMatchesAnyConformingDictionary(self):
        self.assert_matches("quasi-dictionary", has_entry(1, "1"), QuasiDictionary())
        self.assert_does_not_match("non-dictionary", has_entry(1, "1"), object())

    def testHasReadableDescription(self):
        self.assert_description("a dictionary containing ['a': <1>]", has_entry("a", 1))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_entry("a", 1), {"a": 1})

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", has_entry("a", 1), "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", has_entry("a", 1), "bad")

    def test_describe_single_matching_key_mismatching_value(self):
        assert_mismatch_description("value for 'a' was <2>", has_entry("a", 1), {"a": 2})
        assert_mismatch_description(
            "value for 'aa' was <2>", has_entry(starts_with("a"), 1), {"aa": 2}
        )
        assert_mismatch_description(
            "was <{'ab': 2, 'ac': 3}>", has_entry(starts_with("a"), 1), {"ab": 2, "ac": 3}
        )

    def test_describe_match(self):
        assert_match_description("value for 'a' was <1>", has_entry("a", 1), {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()
