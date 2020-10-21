if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.allof import AllOf, all_of
from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AllOfTest(MatcherTest):
    def testMatchesIfArgumentSatisfiesBothOfTwoOtherMatchers(self):
        self.assert_matches("both matchers", all_of(equal_to("good"), equal_to("good")), "good")

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches("both matchers", all_of("good", "good"), "good")

    def testNoMatchIfArgumentFailsToSatisfyEitherOfTwoOtherMatchers(self):
        self.assert_does_not_match(
            "first matcher", all_of(equal_to("bad"), equal_to("good")), "good"
        )
        self.assert_does_not_match(
            "second matcher", all_of(equal_to("good"), equal_to("bad")), "good"
        )
        self.assert_does_not_match(
            "either matcher", all_of(equal_to("bad"), equal_to("bad")), "good"
        )

    def testMatchesIfArgumentSatisfiesAllOfManyOtherMatchers(self):
        self.assert_matches(
            "all matchers",
            all_of(
                equal_to("good"),
                equal_to("good"),
                equal_to("good"),
                equal_to("good"),
                equal_to("good"),
            ),
            "good",
        )

    def testNoMatchIfArgumentFailsToSatisfyAllOfManyOtherMatchers(self):
        self.assert_does_not_match(
            "matcher in the middle",
            all_of(
                equal_to("good"),
                equal_to("good"),
                equal_to("good"),
                equal_to("bad"),
                equal_to("good"),
                equal_to("good"),
            ),
            "good",
        )

    def testHasAReadableDescription(self):
        self.assert_description(
            "('good' and 'bad' and 'ugly')",
            all_of(equal_to("good"), equal_to("bad"), equal_to("ugly")),
        )

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(all_of(equal_to("good"), equal_to("good")), "good")

    def testMismatchDescriptionDescribesFirstFailingMatch(self):
        self.assert_mismatch_description(
            "'good' was 'bad'", all_of(equal_to("bad"), equal_to("good")), "bad"
        )

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
            "'good' was 'bad'", all_of(equal_to("bad"), equal_to("good")), "bad"
        )

    def testMismatchDescriptionOptionallyDescribesMultipleFailingMatches(self):
        self.assert_mismatch_description(
            "'bad' was 'indifferent' and 'good' was 'indifferent'",
            AllOf(
                equal_to("bad"),
                equal_to("indifferent"),
                equal_to("good"),
                describe_all_mismatches=True,
            ),
            "indifferent",
        )


if __name__ == "__main__":
    unittest.main()
