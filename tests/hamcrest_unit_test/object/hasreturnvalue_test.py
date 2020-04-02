if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest import greater_than
from hamcrest.library.object.hasreturnvalue import *
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class MethodsOldStyle:
    def method1(self):
        return "value1"

    def method2(self, arg1):
        return "value{}".format(arg1)

    def method3(self, kwarg1=None):
        return "value{}".format(kwarg1)

    def method4(self, arg1, kwarg1=None):
        return "value{}{}".format(arg1, kwarg1)

    def method5(self, arg1, arg2, kwarg1=None, kwarg2=None):
        return "value{}{}{}{}".format(arg1, arg2, kwarg1, kwarg2)


class MethodsNewStyle(object):
    def method1(self):
        return "value1"

    def method2(self, arg1):
        return "value{}".format(arg1)

    def method3(self, kwarg1=None):
        return "value{}".format(kwarg1)

    def method4(self, arg1, kwarg1=None):
        return "value{}{}".format(arg1, kwarg1)

    def method5(self, arg1, arg2, kwarg1=None, kwarg2=None):
        return "value{}{}{}{}".format(arg1, arg2, kwarg1, kwarg2)

    def __repr__(self):
        return "MethodsNewStyle"

    def __str__(self):
        return repr(self)


class OverridingOldStyle:
    def __getattr__(self, name):
        if name == "method1":
            return lambda: "value1"
        if name == "method2":
            return lambda arg1: "value{}".format(arg1)
        if name == "method3":
            return lambda kwarg1=None: "value{}".format(kwarg1)
        if name == "method4":
            return lambda arg1, kwarg1=None: "value{}{}".format(arg1, kwarg1)
        if name == "method5":
            return lambda arg1, arg2, kwarg1=None, kwarg2=None: "value{}{}{}{}".format(
                arg1, arg2, kwarg1, kwarg2
            )

        raise AttributeError(name)


class OverridingNewStyleGetAttr(object):
    def __getattr__(self, name):
        if name == "method1":
            return lambda: "value1"
        if name == "method2":
            return lambda arg1: "value{}".format(arg1)
        if name == "method3":
            return lambda kwarg1=None: "value{}".format(kwarg1)
        if name == "method4":
            return lambda arg1, kwarg1=None: "value{}{}".format(arg1, kwarg1)
        if name == "method5":
            return lambda arg1, arg2, kwarg1=None, kwarg2=None: "value{}{}{}{}".format(
                arg1, arg2, kwarg1, kwarg2
            )

        raise AttributeError(name)


class OverridingNewStyleGetAttribute(object):
    def __getattribute__(self, name):
        if name == "method1":
            return lambda: "value1"
        if name == "method2":
            return lambda arg1: "value{}".format(arg1)
        if name == "method3":
            return lambda kwarg1=None: "value{}".format(kwarg1)
        if name == "method4":
            return lambda arg1, kwarg1=None: "value{}{}".format(arg1, kwarg1)
        if name == "method5":
            return lambda arg1, arg2, kwarg1=None, kwarg2=None: "value{}{}{}{}".format(
                arg1, arg2, kwarg1, kwarg2
            )

        raise AttributeError(name)


class ObjectReturnValueMatcher(object):

    match_sets = (
        ("old-style: %s", MethodsOldStyle),
        ("new-style: %s", MethodsNewStyle),
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


class HasReturnValueTest(MatcherTest, ObjectReturnValueMatcher):
    def testHasReturnValueWithoutValueMatcher(self):
        self.assert_matches_for_all_types("has method with name", has_return_value("method1"))

    def testHasReturnValueWithoutValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types(
            "has method with name", has_return_value("not_there")
        )

    def testHasReturnValueWithValueMatcher(self):
        self.assert_matches_for_all_types(
            "has method with name and value", has_return_value("method1", "value1")
        )

    def testHasReturnValueWithValueMatcherNegative(self):
        self.assert_does_not_match_for_all_types(
            "has method with name", has_return_value("method1", "not the value")
        )

    def testDescription(self):
        self.assert_description(
            "an object with a method 'method1' whose return value when called with () matches not None",
            has_return_value("method1"),
        )
        self.assert_description(
            "an object with a method 'method1' whose return value when called with () matches 'value1'",
            has_return_value("method1", "value1"),
        )
        self.assert_description(
            "an object with a method 'method2' whose return value when called with (1) matches 'value1'",
            has_return_value("method2", "value1", args=[1]),
        )
        self.assert_description(
            "an object with a method 'method3' whose return value when called with (kwarg1=1) matches 'value1'",
            has_return_value("method3", "value1", kwargs={"kwarg1": 1}),
        )
        self.assert_description(
            "an object with a method 'method4' whose return value when called with (1, kwarg1=1) matches 'value11'",
            has_return_value("method4", "value11", args=[1], kwargs={"kwarg1": 1}),
        )
        self.assert_description(
            "an object with a method 'method5' whose return value when called with (1, 2, kwarg1=1, kwarg2=2) matches 'value1212'",
            has_return_value(
                "method5", "value1212", args=[1, 2], kwargs={"kwarg1": 1, "kwarg2": 2}
            ),
        )

    def testDescribeMissingMethod(self):
        self.assert_mismatch_description(
            "<MethodsNewStyle> did not have a 'not_there' method",
            has_return_value("not_there"),
            MethodsNewStyle(),
        )

    def testDescribeReturnValueMismatch(self):
        self.assert_mismatch_description(
            "method 'method1' called with () was 'value1'",
            has_return_value("method1", "another_value"),
            MethodsNewStyle(),
        )

    def testReturnValueMismatchWithOneArg(self):
        self.assert_describe_mismatch(
            "method 'method2' called with (1) was 'value1'",
            has_return_value("method2", "not the value", args=["1"]),
            MethodsNewStyle(),
        )

    def testReturnValueMismatchWithOneKwarg(self):
        self.assert_describe_mismatch(
            "method 'method3' called with (kwarg1=1) was 'value1'",
            has_return_value("method3", "not the value", kwargs={"kwarg1": 1}),
            MethodsNewStyle(),
        )

    def testReturnValueMismatchWithOneArgAndOneKwarg(self):
        self.assert_describe_mismatch(
            "method 'method4' called with (1, kwarg1=1) was 'value11'",
            has_return_value("method4", "not the value", args=[1], kwargs={"kwarg1": 1}),
            MethodsNewStyle(),
        )

    def testReturnValueMismatchWithMultipleArgsAndKwargs(self):
        self.assert_describe_mismatch(
            "method 'method5' called with (1, 2, kwarg1=1, kwarg2=2) was 'value1212'",
            has_return_value(
                "method5", "not the value", args=[1, 2], kwargs={"kwarg1": 1, "kwarg2": 2}
            ),
            MethodsNewStyle(),
        )

    def testMismatchDescription(self):
        self.assert_describe_mismatch(
            "<MethodsNewStyle> did not have a 'not_there' method",
            has_return_value("not_there"),
            MethodsNewStyle(),
        )

    def testNoMismatchDescriptionOnMatch(self):
        self.assert_no_mismatch_description(
            has_return_value("method1", "value1"), MethodsNewStyle()
        )


if __name__ == "__main__":
    unittest.main()
