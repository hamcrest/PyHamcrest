if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.collection.has_length import *

from hamcrest_unit_test.matcher_test import MatcherTest
from sequencemixin import GeneratorForm, SequenceForm
import unittest

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
        self.assert_matches('empty tuple', matcher, ())
        self.assert_matches('empty list', matcher, [])
        self.assert_matches('emtpy dictionary', matcher, {})

    def testReturnsTrueForEmptyCollectionLike(self):
        matcher = empty()
        self.assert_matches('empty protocol object', matcher, LengthHaver(0))

    def testReturnsFalseForNonEmptyStandardCollections(self):
        matcher = empty()
        self.assert_does_not_match('non-empty tuple', matcher, (1,))
        self.assert_does_not_match('non-empty list', matcher, [1])
        self.assert_does_not_match('emtpy dictionary', matcher, {1:2})

    def testReturnsFalseForNonEmptyCollectionLike(self):
        matcher = empty()
        self.assert_does_not_match('non-empty protocol object', matcher, LengthHaver(1))

    def testHasReadableDescription(self):
        self.assert_description("an empty collection", empty())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(empty(), [])

    def testDescribeMismatch(self):
        self.assert_mismatch_description("has 3 item(s)", empty(), [1,2,3])
        self.assert_mismatch_description("does not support length", empty(), 1)


class HasLengthCollectionTest(MatcherTest):
    def testReturnsTrueForMatchingStandardCollections(self):
        matcher = has_length(1)
        self.assert_matches('tuple', matcher, (1,))
        self.assert_matches('list', matcher, [1])
        self.assert_matches('dictionary', matcher, {1: 2})

    def testReturnsTrueForMatchingCollectionLike(self):
        matcher = has_length(1)
        self.assert_matches('empty protocol object', matcher, LengthHaver(1))

    def testReturnsFalseForNonMatchingStandardCollections(self):
        matcher = has_length(1)
        self.assert_does_not_match('non-empty tuple', matcher, (1, 2))
        self.assert_does_not_match('non-empty list', matcher, [1, 2])
        self.assert_does_not_match('emtpy dictionary', matcher, {1:2, 3:4})

    def testReturnsFalseForNonMatchingCollectionLike(self):
        matcher = has_length(1)
        self.assert_does_not_match('non-empty protocol object', matcher, LengthHaver(2))

    def testHasReadableDescription(self):
        self.assert_description("a collection with 1 item(s)", has_length(1))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_length(1), [1])

    def testDescribeMismatch(self):
        self.assert_mismatch_description("has 3 item(s)", has_length(1), [1,2,3])
        self.assert_mismatch_description("does not support length", has_length(1), 1)