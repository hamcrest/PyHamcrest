if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest
from dataclasses import dataclass
from unittest.mock import Mock

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

    def testSortableKeysKeepSortedDescriptionsAndFirstMismatch(self):
        for matcher in (
            has_entries({"b": 2, "a": 1}),
            has_entries("b", 2, "a", 1),
            has_entries(b=2, a=1),
        ):
            with self.subTest(matcher=matcher):
                self.assert_description("a dictionary containing {'a': <1>, 'b': <2>}", matcher)
                self.assert_mismatch_description("no 'a' key in <{}>", matcher, {})
                self.assert_describe_mismatch("value for 'a' was <0>", matcher, {"b": 0, "a": 0})
        self.assert_description(
            "a dictionary containing {<2>: <2>, <10>: <10>}", has_entries({10: 10, 2: 2})
        )

    def testMixedKeysKeepInputOrderForMatchingAndDescriptions(self):
        expected = {"z": equal_to(3), 1: 2}
        actual = {1: 2, "z": 3}
        expected_items, actual_items = list(expected.items()), list(actual.items())
        matcher = has_entries(expected)
        self.assert_description("a dictionary containing {'z': <3>, <1>: <2>}", matcher)
        self.assert_matches("mixed keys", matcher, actual)
        self.assert_no_mismatch_description(matcher, actual)
        self.assert_mismatch_description("no 'z' key in <{}>", matcher, {})
        self.assert_describe_mismatch("value for 'z' was <0>", matcher, {"z": 0})
        self.assert_mismatch_description("value for <1> was <0>", matcher, {"z": 3, 1: 0})
        self.assertEqual(expected_items, list(expected.items()))
        self.assertEqual(actual_items, list(actual.items()))
        for (_, before), (_, after) in zip(expected_items, expected.items()):
            self.assertIs(before, after)
        for (_, before), (_, after) in zip(actual_items, actual.items()):
            self.assertIs(before, after)

    def testFrozenDataclassKeysNeedNoOrdering(self):
        @dataclass(frozen=True)
        class Key:
            name: str

            def __str__(self):
                return self.name

        matcher = has_entries({Key("b"): 2, Key("a"): 1})
        self.assert_matches("equal distinct keys", matcher, {Key("a"): 1, Key("b"): 2})
        self.assert_description("a dictionary containing {<b>: <2>, <a>: <1>}", matcher)
        self.assert_mismatch_description("no <b> key in <{}>", matcher, {})
        self.assert_describe_mismatch("value for <a> was <0>", matcher, {Key("b"): 2, Key("a"): 0})

    def testFailedSortRetainsEntireOriginalSequence(self):
        matcher = has_entries({3: 3, 1: 1, 2: 2, "a": 4})
        self.assert_description(
            "a dictionary containing {<3>: <3>, <1>: <1>, <2>: <2>, 'a': <4>}", matcher
        )
        self.assert_mismatch_description("no <3> key in <{}>", matcher, {})
        self.assert_matches("all entries retained", matcher, {"a": 4, 2: 2, 1: 1, 3: 3})

    def testValueMatchersFollowStoredOrderAndShortCircuit(self):
        for keys, order in ((["b", "a"], ["a", "b"]), (["z", 1], ["z", 1])):
            with self.subTest(keys=keys):
                calls = []
                values = {}
                for key in keys:
                    value_matcher = equal_to(1)
                    value_matcher.matches = Mock(
                        side_effect=lambda value, key=key: calls.append(key) or value == 1
                    )
                    values[key] = value_matcher
                matcher = has_entries(values)
                self.assert_matches("both evaluated", matcher, dict.fromkeys(keys, 1))
                self.assertEqual(order, calls)
                calls.clear()
                self.assert_does_not_match(
                    "first fails without evaluating second",
                    matcher,
                    {order[0]: 0, order[1]: 1},
                )
                self.assertEqual([order[0]], calls)
                for describe in (self.assert_mismatch_description, self.assert_describe_mismatch):
                    calls.clear()
                    first = "'a'" if order[0] == "a" else "'z'"
                    describe("value for %s was <0>" % first, matcher, {order[0]: 0, order[1]: 1})
                    self.assertEqual([order[0]], calls)
                calls.clear()
                self.assert_does_not_match("second fails", matcher, {order[0]: 1, order[1]: 0})
                self.assertEqual(order, calls)

    def testComparisonTypeErrorFallsBackButOtherErrorsPropagate(self):
        class Key:
            def __init__(self, name, error):
                self.name, self.error = name, error

            def __str__(self):
                return self.name

            def __lt__(self, other):
                raise self.error

        error = TypeError("comparison failure")
        first, second = Key("b", error), Key("a", error)
        matcher = has_entries({first: 2, second: 1})
        self.assert_description("a dictionary containing {<b>: <2>, <a>: <1>}", matcher)
        self.assert_matches("comparison fallback", matcher, {second: 1, first: 2})
        error = RuntimeError("comparison failure")
        with self.assertRaises(RuntimeError) as caught:
            has_entries({Key("b", error): 2, Key("a", error): 1})
        self.assertIs(error, caught.exception)

    def testValueMatcherTypeErrorPropagates(self):
        error = TypeError("matching failure")
        value_matcher = equal_to(1)
        value_matcher.matches = Mock(side_effect=error)
        matcher = has_entries({"z": value_matcher, 1: 2})
        with self.assertRaises(TypeError) as caught:
            matcher.matches({"z": 1, 1: 2})
        self.assertIs(error, caught.exception)

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
