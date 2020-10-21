from hamcrest.library.collection.is_empty import empty
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2012 hamcrest.org"
__license__ = "BSD, see License.txt"


class LengthHaver(object):
    def __init__(self, len_):
        self._len = len_

    def __len__(self):
        return self._len


class EmptyCollectionTest(MatcherTest):
    def testReturnsTrueForEmptyStandardCollections(self):
        matcher = empty()
        self.assert_matches("empty tuple", matcher, ())
        self.assert_matches("empty list", matcher, [])
        self.assert_matches("emtpy dictionary", matcher, {})

    def testReturnsTrueForEmptyCollectionLike(self):
        matcher = empty()
        self.assert_matches("empty protocol object", matcher, LengthHaver(0))

    def testReturnsFalseForNonEmptyStandardCollections(self):
        matcher = empty()
        self.assert_does_not_match("non-empty tuple", matcher, (1,))
        self.assert_does_not_match("non-empty list", matcher, [1])
        self.assert_does_not_match("emtpy dictionary", matcher, {1: 2})

    def testReturnsFalseForNonEmptyCollectionLike(self):
        matcher = empty()
        self.assert_does_not_match("non-empty protocol object", matcher, LengthHaver(1))

    def testHasReadableDescription(self):
        self.assert_description("an empty collection", empty())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(empty(), [])

    def testDescribeMismatch(self):
        self.assert_mismatch_description("has 3 item(s)", empty(), [1, 2, 3])
        self.assert_mismatch_description("does not support length", empty(), 1)
