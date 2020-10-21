if __name__ == "__main__":
    import sys

    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.integration.match_equality import match_equality, tostring

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class MatchEqualityWrapperTest(unittest.TestCase):
    def testMatcherIsEqualWhenMatchesIsTrue(self):
        matcher = equal_to("bar")
        assert match_equality(matcher) == "bar"

    def testMatcherIsNotEqualWhenMatchesIsFalse(self):
        matcher = equal_to("bar")
        assert match_equality(matcher) != "foo"

    def testMatcherStringIsMatcherDescription(self):
        matcher = equal_to("bar")
        assert str(match_equality(matcher)) == tostring(matcher)

    def testMatcherReprIsMatcher(self):
        matcher = equal_to("bar")
        assert repr(match_equality(matcher)) == tostring(matcher)

    def testMatchesWhenProvidedAnObject(self):
        assert match_equality("bar") == "bar"


if __name__ == "__main__":
    unittest.main()
