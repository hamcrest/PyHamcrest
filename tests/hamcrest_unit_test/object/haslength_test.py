if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.number.ordering_comparison import greater_than
from hamcrest.library.object.haslength import has_length
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class FakeWithLen(object):
    def __init__(self, len):
        self.len = len

    def __len__(self):
        return self.len

    def __str__(self):
        return "FakeWithLen"


class FakeWithoutLen(object):
    def __str__(self):
        return "FakeWithoutLen"


class HasLengthTest(MatcherTest):
    def testPassesResultOfLenToNestedMatcher(self):
        self.assert_matches("equal", has_length(equal_to(42)), FakeWithLen(42))
        self.assert_does_not_match("unequal", has_length(equal_to(42)), FakeWithLen(1))

    def testProvidesConvenientShortcutForHasLengthEqualTo(self):
        self.assert_matches("equal", has_length(42), FakeWithLen(42))
        self.assert_does_not_match("unequal", has_length(42), FakeWithLen(1))

    def testDoesNotMatchObjectWithoutLen(self):
        self.assert_does_not_match("no length", has_length(42), object())

    def testHasReadableDescription(self):
        self.assert_description(
            "an object with length of a value greater than <5>", has_length(greater_than(5))
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_length(3), "foo")

    def testMismatchDescriptionForItemWithWrongLength(self):
        self.assert_mismatch_description(
            "was <FakeWithLen> with length of <4>", has_length(3), FakeWithLen(4)
        )

    def testMismatchDescriptionForItemWithoutLength(self):
        self.assert_mismatch_description("was <FakeWithoutLen>", has_length(3), FakeWithoutLen())

    def testDescribeMismatchForItemWithWrongLength(self):
        self.assert_describe_mismatch(
            "was <FakeWithLen> with length of <4>", has_length(3), FakeWithLen(4)
        )

    def testDescribeMismatchForItemWithoutLength(self):
        self.assert_describe_mismatch("was <FakeWithoutLen>", has_length(3), FakeWithoutLen())


if __name__ == "__main__":
    unittest.main()
