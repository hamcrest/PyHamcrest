if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.anyof import any_of
from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AnyOfTest(MatcherTest):
    def testMatchesIfArgumentSatisfiesEitherOrBothOfTwoOtherMatchers(self):
        self.assert_matches("first matcher", any_of(equal_to("good"), equal_to("bad")), "good")
        self.assert_matches("second matcher", any_of(equal_to("bad"), equal_to("good")), "good")
        self.assert_matches("both matchers", any_of(equal_to("good"), equal_to("good")), "good")

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches("first matcher", any_of("good", "bad"), "good")
        self.assert_matches("second matcher", any_of("bad", "good"), "good")
        self.assert_matches("both matchers", any_of("good", "good"), "good")

    def testNoMatchIfArgumentFailsToSatisfyEitherOfTwoOtherMatchers(self):
        self.assert_does_not_match(
            "either matcher", any_of(equal_to("bad"), equal_to("bad")), "good"
        )

    def testMatchesIfArgumentSatisfiesAnyOfManyOtherMatchers(self):
        self.assert_matches(
            "matcher in the middle",
            any_of(
                equal_to("bad"), equal_to("bad"), equal_to("good"), equal_to("bad"), equal_to("bad")
            ),
            "good",
        )

    def testNoMatchIfArgumentFailsToSatisfyAnyOfManyOtherMatchers(self):
        self.assert_does_not_match(
            "all matchers",
            any_of(
                equal_to("bad"), equal_to("bad"), equal_to("bad"), equal_to("bad"), equal_to("bad")
            ),
            "good",
        )

    def testHasAReadableDescription(self):
        self.assert_description(
            "('good' or 'bad' or 'ugly')",
            any_of(equal_to("good"), equal_to("bad"), equal_to("ugly")),
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(any_of(equal_to("good"), equal_to("bad")), "good")

    def testMismatchDescriptionDescribesFirstFailingMatch(self):
        self.assert_mismatch_description(
            "was 'ugly'", any_of(equal_to("bad"), equal_to("good")), "ugly"
        )

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
            "was 'ugly'", any_of(equal_to("bad"), equal_to("good")), "ugly"
        )


if __name__ == "__main__":
    unittest.main()
