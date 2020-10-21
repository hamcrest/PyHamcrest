if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest import greater_than
from hamcrest.library.object.hasproperty import has_properties, has_property
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class OnePropertyOldStyle:

    field = "value"
    field2 = "value2"


class ThreePropertiesNewStyle(object):

    field = "value"
    field2 = "value2"
    field3 = "value3"

    def __repr__(self):
        return "ThreePropertiesNewStyle"

    def __str__(self):
        return repr(self)


class OverridingOldStyle:
    def __getattr__(self, name):
        if name == "field":
            return "value"
        if name == "field2":
            return "value2"

        raise AttributeError(name)


class OverridingNewStyleGetAttr(object):
    def __getattr__(self, name):
        if name == "field":
            return "value"
        if name == "field2":
            return "value2"

        raise AttributeError(name)


class OverridingNewStyleGetAttribute(object):
    def __getattribute__(self, name):
        if name == "field":
            return "value"
        if name == "field2":
            return "value2"

        raise AttributeError(name)


class ObjectPropertyMatcher(object):

    match_sets = (
        ("old-style: %s", OnePropertyOldStyle),
        ("new-style: %s", ThreePropertiesNewStyle),
        ("old-style, overriding: %s", OverridingOldStyle),
        ("new-style, using getattr: %s", OverridingNewStyleGetAttr),
        ("new-style, using getattribute: %s", OverridingNewStyleGetAttribute),
    )

    def assert_matches_for_all_types(self, description, matcher):
        for description_fmt, target_class in self.match_sets:
            self.assert_matches(description_fmt % description, matcher, target_class())

    def assert_does_not_match_for_all_types(self, description, matcher):
        for description_fmt, target_class in self.match_sets:
            self.assert_does_not_match(description_fmt % description, matcher, target_class())


class HasPropertyTest(MatcherTest, ObjectPropertyMatcher):
    def testHasPropertyWithoutValueMatcher(self):
        self.assert_matches_for_all_types("has property with name", has_property("field"))

    def testHasPropertyWithoutValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types(
            "has property with name", has_property("not_there")
        )

    def testHasPropertyWithValueMatcher(self):
        self.assert_matches_for_all_types(
            "has property with name and value", has_property("field", "value")
        )

    def testHasPropertyWithValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types(
            "has property with name", has_property("field", "not the value")
        )

    def testDescription(self):
        self.assert_description(
            "an object with a property 'field' matching ANYTHING", has_property("field")
        )
        self.assert_description(
            "an object with a property 'field' matching 'value'", has_property("field", "value")
        )

    def testDescribeMissingProperty(self):
        self.assert_mismatch_description(
            "<ThreePropertiesNewStyle> did not have the 'not_there' property",
            has_property("not_there"),
            ThreePropertiesNewStyle(),
        )

    def testDescribePropertyValueMismatch(self):
        self.assert_mismatch_description(
            "property 'field' was 'value'",
            has_property("field", "another_value"),
            ThreePropertiesNewStyle(),
        )

    def testMismatchDescription(self):
        self.assert_describe_mismatch(
            "<ThreePropertiesNewStyle> did not have the 'not_there' property",
            has_property("not_there"),
            ThreePropertiesNewStyle(),
        )

    def testNoMismatchDescriptionOnMatch(self):
        self.assert_no_mismatch_description(
            has_property("field", "value"), ThreePropertiesNewStyle()
        )


class HasPropertiesTest(MatcherTest, ObjectPropertyMatcher):
    def testMatcherCreationRequiresEvenNumberOfPositionalArguments(self):
        self.assertRaises(ValueError, has_properties, "a", "b", "c")

    def testMatchesUsingSingleDictionaryArgument(self):
        # import pdb; pdb.set_trace()
        self.assert_matches_for_all_types(
            "matches using a single-argument dictionary",
            has_properties({"field": "value", "field2": "value2"}),
        )

    def testMatchesUsingKeywordArguments(self):
        self.assert_matches_for_all_types(
            "matches using a kwarg dict", has_properties(field="value", field2="value2")
        )

    def testMismatchDescription(self):
        self.assert_describe_mismatch(
            "property 'field' was 'value' and property 'field3' was 'value3'",
            has_properties(field="different", field2="value2", field3="alsodifferent"),
            ThreePropertiesNewStyle(),
        )

    def testDescription(self):
        self.assert_description("an object with a property 'a' matching <1>", has_properties(a=1))
        self.assert_description(
            "an object with properties 'a' matching <1> "
            "and 'b' matching a value greater than <2>",
            has_properties(a=1, b=greater_than(2)),
        )


if __name__ == "__main__":
    unittest.main()
