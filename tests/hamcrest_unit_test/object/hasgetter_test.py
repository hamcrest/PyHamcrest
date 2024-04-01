import typing

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest import greater_than
from hamcrest.library.object.hasgetter import has_getters, has_getter
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Chris Rose;Thomas Hess"
__copyright__ = "Copyright 2024 hamcrest.org"
__license__ = "BSD, see License.txt"


class StaticMethodGetter:
    @staticmethod
    def field() -> str:
        return "value"

    @staticmethod
    def field2() -> str:
        return "value2"


class NonCallableProperty:
    field = "value"

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return repr(self)


class MethodGetter:
    def field(self) -> str:
        return "value"

    def field2(self) -> str:
        return "value2"

    def field3(self) -> str:
        return "value3"

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return repr(self)


class OverridingGetAttr:
    def __getattr__(self, name):
        if name == "field":
            return lambda: "value"
        if name == "field2":
            return lambda: "value2"

        raise AttributeError(name)


class OverridingGetAttribute:
    def __getattribute__(self, name):
        if name == "field":
            return lambda: "value"
        if name == "field2":
            return lambda: "value2"

        raise AttributeError(name)


class ObjectGetterMatcher(object):
    match_sets: typing.Tuple[typing.Tuple[str, typing.Type]] = (
        ("static-method: {}", StaticMethodGetter),
        ("method: {}", MethodGetter),
        ("using getattr: {}", OverridingGetAttr),
        ("using getattribute: {}", OverridingGetAttribute),
    )

    def assert_matches_for_all_types(self, description, matcher):
        for description_fmt, target_class in self.match_sets:
            self.assert_matches(description_fmt.format(description), matcher, target_class())

    def assert_does_not_match_for_all_types(self, description, matcher):
        for description_fmt, target_class in self.match_sets:
            self.assert_does_not_match(description_fmt.format(description), matcher, target_class())


class HasGetterTest(MatcherTest, ObjectGetterMatcher):
    def testHasPropertyWithoutValueMatcher(self):
        self.assert_matches_for_all_types("has getter with name", has_getter("field"))

    def testHasGetterWithoutValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types("has getter with name", has_getter("not_there"))

    def testHasGetterWithValueMatcher(self):
        self.assert_matches_for_all_types(
            "has getter with name and value", has_getter("field", "value")
        )

    def testHasGetterWithValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types(
            "has getter with name", has_getter("field", "not the value")
        )

    def testHasGetterWithNonCallableProperty(self):
        self.assert_does_not_match(
            "<NonCallableProperty> attribute 'field' is not callable",
            has_getter("field"),
            NonCallableProperty(),
        )

    def testDescription(self):
        self.assert_description(
            "an object with a getter 'field' returning ANYTHING", has_getter("field")
        )
        self.assert_description(
            "an object with a getter 'field' returning 'value'", has_getter("field", "value")
        )

    def testDescribeMissingGetter(self):
        self.assert_mismatch_description(
            "<MethodGetter> did not have the 'not_there' getter",
            has_getter("not_there"),
            MethodGetter(),
        )

    def testDescribeNonCallableProperty(self):
        self.assert_mismatch_description(
            "<NonCallableProperty> attribute 'field' is not callable",
            has_getter("field"),
            NonCallableProperty(),
        )

    def testDescribeGetterValueMismatch(self):
        self.assert_mismatch_description(
            "getter 'field' return value was 'value'",
            has_getter("field", "another_value"),
            MethodGetter(),
        )

    def testMismatchDescription(self):
        self.assert_describe_mismatch(
            "<MethodGetter> did not have the 'not_there' getter",
            has_getter("not_there"),
            MethodGetter(),
        )

    def testNoMismatchDescriptionOnMatch(self):
        self.assert_no_mismatch_description(has_getter("field", "value"), MethodGetter())


class HasPropertiesTest(MatcherTest, ObjectGetterMatcher):
    def testMatcherCreationRequiresEvenNumberOfPositionalArguments(self):
        self.assertRaises(ValueError, has_getters, "a", "b", "c")

    def testMatchesUsingSingleDictionaryArgument(self):
        # import pdb; pdb.set_trace()
        self.assert_matches_for_all_types(
            "matches using a single-argument dictionary",
            has_getters({"field": "value", "field2": "value2"}),
        )

    def testMatchesUsingKeywordArguments(self):
        self.assert_matches_for_all_types(
            "matches using a kwarg dict", has_getters(field="value", field2="value2")
        )

    def testMismatchDescription(self):
        self.assert_describe_mismatch(
            "getter 'field' return value was 'value' and getter 'field3' return value was 'value3'",
            has_getters(field="different", field2="value2", field3="alsodifferent"),
            MethodGetter(),
        )

    def testDescription(self):
        self.assert_description("an object with a getter 'a' returning <1>", has_getters(a=1))
        self.assert_description(
            "an object with getters 'a' returning <1> "
            "and 'b' returning a value greater than <2>",
            has_getters(a=1, b=greater_than(2)),
        )


if __name__ == "__main__":
    unittest.main()
