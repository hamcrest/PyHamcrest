import unittest

from hamcrest.library.text.stringendswith import ends_with
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


EXCERPT = "EXCERPT"
matcher = ends_with(EXCERPT)


class StringEndsWithTest(MatcherTest):
    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assert_does_not_match("excerpt at beginning", matcher, EXCERPT + "END")
        self.assert_matches("excerpt at end", matcher, "START" + EXCERPT)
        self.assert_does_not_match("excerpt in middle", matcher, "START" + EXCERPT + "END")
        self.assert_matches("excerpt repeated", matcher, EXCERPT + EXCERPT)

        self.assert_does_not_match("excerpt not in string", matcher, "whatever")
        self.assert_does_not_match("only part of excerpt is at end of string", matcher, EXCERPT[1:])

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assert_matches("excerpt is entire string", matcher, EXCERPT)

    def testMatcherCreationRequiresString(self):
        self.assertRaises(TypeError, ends_with, 3)

    def testFailsIfMatchingAgainstNonString(self):
        self.assert_does_not_match("non-string", matcher, object())

    def testHasAReadableDescription(self):
        self.assert_description("a string ending with 'EXCERPT'", matcher)

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(matcher, EXCERPT)

    def testMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", matcher, "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", matcher, "bad")


if __name__ == "__main__":
    unittest.main()
