if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import re
import unittest

from hamcrest.library.text.stringmatches import matches_regexp
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

string_matcher = matches_regexp(r"--[a-z]+--")
compiled_matcher = matches_regexp(re.compile(r"--[a-z]+--"))


class StringMatchesTest(MatcherTest):
    def testMatchesWhenPatternIsFoundAtBeginning(self):
        self.assert_matches("pattern at beginning", string_matcher, "--a-----")

    def testMatchesWhenPatternIsFoundAtEnd(self):
        self.assert_matches("pattern at end", string_matcher, "-----a--")

    def testMatchesWhenPatternIsFoundInMiddle(self):
        self.assert_matches("pattern in the middle", string_matcher, "-----a-----")

    def testMismatchesWhenPatternIsNotPresent(self):
        self.assert_does_not_match("pattern nowhere", string_matcher, "--0--")

    def testMatchesUsingCompiledExpressions(self):
        self.assert_matches("pattern nowhere", compiled_matcher, "--a--")

    def testMismatchesUsingCompiledExpressions(self):
        self.assert_does_not_match("pattern nowhere", compiled_matcher, "--0--")

    def testStringHasAReadableDescription(self):
        self.assert_description("a string matching '--[a-z]+--'", string_matcher)

    def testPatternHasAReadableDescription(self):
        self.assert_description("a string matching '--[a-z]+--'", compiled_matcher)

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(string_matcher, "--a--")

    def testStringMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", string_matcher, "bad")

    def testCompiledMismatchDescription(self):
        self.assert_mismatch_description("was 'bad'", compiled_matcher, "bad")

    def testStringDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", string_matcher, "bad")

    def testCompiledDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", compiled_matcher, "bad")


if __name__ == "__main__":
    unittest.main()
