if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.library.sequence.issequence_containing import hasitem, hasitems

from matcher_test import MatcherTest
from quasisequence import QuasiSequence


class IsSequenceContainingTest(MatcherTest):

    def testMatchesASequenceThatContainsAnElementMatchingTheGivenMatcher(self):
        self.assert_matches("should match sequence that contains 'a'",
                            hasitem(equalto('a')), ['a', 'b', 'c'])

    def testDoesNotMatchASequenceThatDoesntContainAnElementMatchingTheGivenMatcher(self):
        self.assert_does_not_match("should not matche sequence that doesn't contain 'a'",
                                    hasitem(equalto('a')), ['b', 'c'])
        self.assert_does_not_match('should not match empty sequence',
                                    hasitem(equalto('a')), [])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches("should match sequence that contains 'a'",
                            hasitem('a'), ['a', 'b', 'c'])
        self.assert_does_not_match("should not match sequence that doesn't contain 'a'",
                                    hasitem('a'), ['b', 'c'])

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing 'a'", hasitem('a'))

    def testMatchesAllItemsInCollection(self):
        matcher1 = hasitems(equalto('a'), equalto('b'), equalto('c'))
        self.assert_matches('should match sequence containing all items',
                            matcher1, ('a', 'b', 'c'))
        
        matcher2 = hasitems('a', 'b', 'c')
        self.assert_matches('should match sequence containing all items (without matchers)',
                            matcher2, ('a', 'b', 'c'))
        
        matcher3 = hasitems(equalto('a'), equalto('b'), equalto('c'))
        self.assert_matches('should match sequence containing all items in any order',
                            matcher3, ('c', 'b', 'a'))
        
        matcher4 = hasitems(equalto('a'), equalto('b'), equalto('c'))
        self.assert_matches('should match sequence containing all items plus others',
                            matcher4, ('e', 'c', 'b', 'a', 'd'))
        
        matcher5 = hasitems(equalto('a'), equalto('b'), equalto('c'))
        self.assert_does_not_match('should not match sequence unless it contains all items',
                            matcher5, ('e', 'c', 'b', 'd')) # 'a' missing

    def testMatchesQuasiSequence(self):
        quasi = QuasiSequence()
        self.assert_matches('quasi', hasitem(1), quasi)
        self.assert_does_not_match('other', hasitem(1), object())


if __name__ == '__main__':
    unittest.main()
