__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.issequence_containing import has_item, has_items

from matcher_test import MatcherTest
from quasisequence import QuasiSequence


class IsSequenceContainingTest(MatcherTest):

    def testMatchesASequenceThatContainsAnElementMatchingTheGivenMatcher(self):
        self.assert_matches("should match sequence that contains 'a'",
                            has_item(equal_to('a')), ['a', 'b', 'c'])

    def testDoesNotMatchASequenceThatDoesntContainAnElementMatchingTheGivenMatcher(self):
        self.assert_does_not_match("should not matche sequence that doesn't contain 'a'",
                                    has_item(equal_to('a')), ['b', 'c'])
        self.assert_does_not_match('should not match empty sequence',
                                    has_item(equal_to('a')), [])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches("should match sequence that contains 'a'",
                            has_item('a'), ['a', 'b', 'c'])
        self.assert_does_not_match("should not match sequence that doesn't contain 'a'",
                                    has_item('a'), ['b', 'c'])

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing 'a'", has_item('a'))

    def testMatchesAllItemsInCollection(self):
        matcher1 = has_items(equal_to('a'), equal_to('b'), equal_to('c'))
        self.assert_matches('should match sequence containing all items',
                            matcher1, ('a', 'b', 'c'))

        matcher2 = has_items('a', 'b', 'c')
        self.assert_matches('should match sequence containing all items (without matchers)',
                            matcher2, ('a', 'b', 'c'))

        matcher3 = has_items(equal_to('a'), equal_to('b'), equal_to('c'))
        self.assert_matches('should match sequence containing all items in any order',
                            matcher3, ('c', 'b', 'a'))

        matcher4 = has_items(equal_to('a'), equal_to('b'), equal_to('c'))
        self.assert_matches('should match sequence containing all items plus others',
                            matcher4, ('e', 'c', 'b', 'a', 'd'))

        matcher5 = has_items(equal_to('a'), equal_to('b'), equal_to('c'))
        self.assert_does_not_match('should not match sequence unless it contains all items',
                            matcher5, ('e', 'c', 'b', 'd')) # 'a' missing

    def testMatchesAnyConformingSequence(self):
        self.assert_matches('quasi-sequence', has_item(1), QuasiSequence())
        self.assert_does_not_match('non-sequence', has_item(1), object())


if __name__ == '__main__':
    unittest.main()
