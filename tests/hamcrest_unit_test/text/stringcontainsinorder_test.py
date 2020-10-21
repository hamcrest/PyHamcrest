from hamcrest.library.text import string_contains_in_order
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Romilly Cocking"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


matcher = string_contains_in_order("string one", "string two", "string three")


class StringContainsInOrderTest(MatcherTest):
    def testMatchesIfOrderIsCorrect(self):
        self.assert_matches(
            "correct order", matcher, "string one then string two followed by string three"
        )

    def testDoesNotMatchIfOrderIsIncorrect(self):
        self.assert_does_not_match(
            "incorrect order", matcher, "string two then string one followed by string three"
        )

    def testDoesNotMatchIfExpectedSubstringsAreMissing(self):
        self.assert_does_not_match("missing string one", matcher, "string two then string three")
        self.assert_does_not_match("missing string two", matcher, "string one then string three")
        self.assert_does_not_match("missing string three", matcher, "string one then string two")

    def testMatcherCreationRequiresString(self):
        self.assertRaises(TypeError, string_contains_in_order, 3)

    def testFailsIfMatchingAgainstNonString(self):
        self.assert_does_not_match("non-string", matcher, object())

    def testHasAReadableDescription(self):
        self.assert_description(
            "a string containing 'string one', 'string two', 'string three' in order", matcher
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(
            matcher, "string one then string two followed by string three"
        )

    def testMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", matcher, "bad")

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", matcher, "bad")
