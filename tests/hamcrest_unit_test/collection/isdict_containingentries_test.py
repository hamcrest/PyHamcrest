if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containingentries import has_entries
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingEntriesTest(MatcherTest):
    def testMatcherCreationRequiresEvenNumberOfPositionalArgs(self):
        self.assertRaises(ValueError, has_entries, "a", "b", "c")

    def testDoesNotMatchNonDictionary(self):
        self.assert_does_not_match("non-dictionary", has_entries("a", equal_to(1)), object())

    def testMatchesDictLike(self):
        class DictLike(object):
            def __getitem__(self, key):
                return "value: " + str(key)

            def __contains__(self, key):
                return True

        self.assert_matches(
            "matches a dictionary-like object", has_entries("a", equal_to("value: a")), DictLike()
        )

    def testMatchesUsingSingleDictionaryArgument(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries({"a": equal_to(1), "b": equal_to(2)}), target)
        self.assert_matches("has c & a", has_entries({"c": equal_to(3), "a": equal_to(1)}), target)
        self.assert_does_not_match(
            "no d:3", has_entries({"b": equal_to(2), "d": equal_to(3)}), target
        )

    def testMatcheSingleDictionaryArgumentWithImplicitEqualTo(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries({"a": 1, "b": 2}), target)
        self.assert_matches("has c & a", has_entries({"c": 3, "a": 1}), target)
        self.assert_does_not_match("no d:3", has_entries({"b": 2, "d": 3}), target)

    def testMatchesUsingKwargs(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries(a=equal_to(1), b=equal_to(2)), target)
        self.assert_matches("has c & a", has_entries(c=equal_to(3), a=equal_to(1)), target)
        self.assert_does_not_match("no d:3", has_entries(b=equal_to(2), d=equal_to(3)), target)

    def testMatchesKwargsWithImplicitEqualTo(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries(a=1, b=2), target)
        self.assert_matches("has c & a", has_entries(c=3, a=1), target)
        self.assert_does_not_match("no d:3", has_entries(b=2, d=3), target)

    def testMatchesDictionaryContainingSingleKeyWithMatchingValue(self):
        target = {"a": 1, "b": 2}
        self.assert_matches("has a:1", has_entries("a", equal_to(1)), target)
        self.assert_matches("has b:2", has_entries("b", equal_to(2)), target)
        self.assert_does_not_match("no b:3", has_entries("b", equal_to(3)), target)
        self.assert_does_not_match("no c:2", has_entries("c", equal_to(2)), target)

    def testMatchesDictionaryContainingMultipleKeysWithMatchingValues(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries("a", equal_to(1), "b", equal_to(2)), target)
        self.assert_matches("has c & a", has_entries("c", equal_to(3), "a", equal_to(1)), target)
        self.assert_does_not_match(
            "no d:3", has_entries("b", equal_to(3), "d", equal_to(3)), target
        )

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        target = {"a": 1, "b": 2, "c": 3}
        self.assert_matches("has a & b", has_entries("a", 1, "b", 2), target)
        self.assert_matches("has c & a", has_entries("c", 3, "a", 1), target)
        self.assert_does_not_match("no d:4", has_entries("b", 3, "d", 4), target)

    def testHasReadableDescription(self):
        self.assert_description(
            "a dictionary containing {'a': <1>, 'b': <2>}", has_entries("a", 1, "b", 2)
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_entries("a", 1), {"a": 1})

    def testMismatchDescriptionOfNonDictionaryShowsActualArgument(self):
        self.assert_mismatch_description(
            "'bad' is not a mapping object", has_entries("a", 1), "bad"
        )

    def testMismatchDescriptionOfDictionaryWithNonMatchingValue(self):
        self.assert_mismatch_description("value for 'a' was <2>", has_entries("a", 1), {"a": 2})

    def testDescribeMismatchOfNonDictionaryShowsActualArgument(self):
        self.assert_describe_mismatch("'bad' is not a mapping object", has_entries("a", 1), "bad")

    def testDescribeMismatchOfDictionaryWithoutKey(self):
        d = {"a": 1, "c": 3}
        self.assert_describe_mismatch("no 'b' key in <%s>" % (d,), has_entries("a", 1, "b", 2), d)

    def testDescribeMismatchOfDictionaryWithNonMatchingValue(self):
        self.assert_describe_mismatch("value for 'a' was <2>", has_entries("a", 1), {"a": 2})


if __name__ == "__main__":
    unittest.main()
