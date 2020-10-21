if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object.hasstring import has_string
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class FakeWithStr(object):
    def __str__(self):
        return "FakeWithStr"


class HasStringTest(MatcherTest):
    def testPassesResultOfToStrToNestedMatcher(self):
        self.assert_matches("equal", has_string(equal_to("FakeWithStr")), FakeWithStr())
        self.assert_does_not_match("unequal", has_string(equal_to("FakeWithStr")), 3)

    def testProvidesConvenientShortcutForHasStringEqualTo(self):
        self.assert_matches("equal", has_string("FakeWithStr"), FakeWithStr())
        self.assert_does_not_match("unequal", has_string("FakeWithStr"), 3)

    def testHasReadableDescription(self):
        self.assert_description("an object with str 'foo'", has_string("foo"))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_string("FakeWithStr"), FakeWithStr())

    def testMismatchDescription(self):
        self.assert_mismatch_description("was <FakeWithStr>", has_string("foo"), FakeWithStr())

    def testDescribeMismatchDescription(self):
        self.assert_describe_mismatch("was <FakeWithStr>", has_string("foo"), FakeWithStr())


if __name__ == "__main__":
    unittest.main()
