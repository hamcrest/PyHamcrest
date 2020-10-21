if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isanything import anything
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsAnythingTest(MatcherTest):
    def testAlwaysEvaluatesToTrue(self):
        self.assert_matches("None", anything(), None)
        self.assert_matches("object", anything(), object())
        self.assert_matches("string", anything(), "hi")

    def testHasUsefulDefaultDescription(self):
        self.assert_description("ANYTHING", anything())

    def testCanOverrideDescription(self):
        description = "DESCRIPTION"
        self.assert_description(description, anything(description))

    def testMatchAlwaysSucceedsSoShouldNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(anything(), "hi")


if __name__ == "__main__":
    unittest.main()
