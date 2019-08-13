import unittest

from hamcrest.library.text.isequal_ignoring_case import equal_to_ignoring_case
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


matcher = equal_to_ignoring_case("heLLo")


class IsEqualIgnoringCaseTest(MatcherTest):
    def testIgnoresCaseOfCharsInString(self):
        self.assert_matches("all upper", matcher, "HELLO")
        self.assert_matches("all lower", matcher, "hello")
        self.assert_matches("mixed up", matcher, "HelLo")

        self.assert_does_not_match("no match", matcher, "bye")

    def testFailsIfAdditionalWhitespaceIsPresent(self):
        self.assert_does_not_match("whitespace suffix", matcher, "heLLo ")
        self.assert_does_not_match("whitespace prefix", matcher, " heLLo")

    def testMatcherCreationRequiresString(self):
        self.assertRaises(TypeError, equal_to_ignoring_case, 3)

    def testFailsIfMatchingAgainstNonString(self):
        self.assert_does_not_match("non-string", matcher, object())

    def testHasAReadableDescription(self):
        self.assert_description("'heLLo' ignoring case", matcher)

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(matcher, "hello")

    def testMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", matcher, "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", matcher, "bad")


if __name__ == "__main__":
    unittest.main()
