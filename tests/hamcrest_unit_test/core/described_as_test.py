import unittest

from hamcrest.core.core.described_as import described_as
from hamcrest.core.core.isanything import anything
from hamcrest_unit_test.matcher_test import MatcherTest

from .nevermatch import NeverMatch

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class DescribedAsTest(MatcherTest):
    def testOverridesDescriptionOfNestedMatcherWithConstructorArgument(self):
        m1 = described_as("m1 description", anything())
        m2 = described_as("m2 description", NeverMatch())

        self.assert_description("m1 description", m1)
        self.assert_description("m2 description", m2)

    def testAppendsValuesToDescription(self):
        m = described_as("value 1 = %0, value 2 = %1", anything(), 33, 97)

        self.assert_description("value 1 = <33>, value 2 = <97>", m)

    def testDelegatesMatchingToNestedMatcher(self):
        m1 = described_as("irrelevant", anything())
        m2 = described_as("irrelevant", NeverMatch())

        self.assertTrue(m1.matches(object()))
        self.assertTrue(not m2.matches("hi"))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(described_as("irrelevant", anything()), object())

    def testDelegatesMismatchDescriptionToNestedMatcher(self):
        self.assert_mismatch_description(
            NeverMatch.mismatch_description, described_as("irrelevant", NeverMatch()), "hi"
        )

    def testDelegatesDescribeMismatchToNestedMatcher(self):
        self.assert_describe_mismatch(
            NeverMatch.mismatch_description, described_as("irrelevant", NeverMatch()), "hi"
        )


if __name__ == "__main__":
    unittest.main()
