if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.collection.issequence_containing import *

from hamcrest.core.core.isequal import equal_to
from matcher_test import MatcherTest
from quasisequence import QuasiSequence
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceContainingTest(MatcherTest):

    def testMatchesASequenceThatContainsAnElementMatchingTheGivenMatcher(self):
        self.assert_matches("sequence contains 'a'",
                            has_item(equal_to('a')), ['a', 'b', 'c'])

    def testNoMatchIfSequenceDoesntContainAnElementMatchingTheGivenMatcher(self):
        self.assert_does_not_match("sequence without 'a'",
                                    has_item(equal_to('a')), ['b', 'c'])
        self.assert_does_not_match('empty', has_item(equal_to('a')), [])

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches("sequence contains 'a'",
                            has_item('a'), ['a', 'b', 'c'])
        self.assert_does_not_match("sequence without 'a'",
                                   has_item('a'), ['b', 'c'])

    def testMatchesAnyConformingSequence(self):
        self.assert_matches('quasi-sequence', has_item(1), QuasiSequence())
        self.assert_does_not_match('non-sequence', has_item(1), object())

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing 'a'", has_item('a'))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_item('a'), ['a', 'b'])

    def testMismatchDescriptionShowsActualArgument(self):
        self.assert_mismatch_description("was <42>", has_item('a'), 42)

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was <42>", has_item('a'), 42)


class IsSequenceContainingItemsTest(MatcherTest):

    def testShouldMatchCollectionContainingAllItems(self):
        self.assert_matches('contains all items',
                            has_items(equal_to('a'), equal_to('b'), equal_to('c')),
                            ('a', 'b', 'c'))

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches('Values automatically wrapped with equal_to',
                            has_items('a', 'b', 'c'),
                            ('a', 'b', 'c'))

    def testShouldMatchCollectionContainingAllItemsInDifferentOrder(self):
        self.assert_matches('all items in different order',
                            has_items('a', 'b', 'c'),
                            ('c', 'b', 'a'))

    def testShouldMatchCollectionContainingAllItemsPlusExtras(self):
        self.assert_matches('all items plus extras',
                            has_items('a', 'b', 'c'),
                            ('e', 'c', 'b', 'a', 'd'))

    def testNoMatchIfCollectionDoesntSatisfyAllMatchers(self):
        self.assert_does_not_match("missing 'a'",
                                   has_items('a', 'b', 'c'),
                                   ('e', 'c', 'b', 'd'))

    def testHasAReadableDescription(self):
        self.assert_description(
            "(a sequence containing 'a' and a sequence containing 'b')",
            has_items('a', 'b'))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_items('a', 'b'), ['a', 'b'])

    def testMismatchDescriptionShowsFirstUnmetMatcherAndActualArgument(self):
        self.assert_mismatch_description("a sequence containing 'a' was <42>",
                                         has_items('a', 'b'), 42)

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("a sequence containing 'a' was <42>",
                                      has_items('a', 'b'), 42)


if __name__ == '__main__':
    unittest.main()
