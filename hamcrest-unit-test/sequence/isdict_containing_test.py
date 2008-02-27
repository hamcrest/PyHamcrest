if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.sequence.isdict_containing import has_entry

from matcher_test import MatcherTest
from quasidict import QuasiDictionary


class IsDictContainingTest(MatcherTest):

    def testMatchesDictContainingMatchingKeyAndValue(self):
        d = {'a': 1, 'b': 2}
        self.assert_matches('matcherA', has_entry(equal_to('a'), equal_to(1)), d)
        self.assert_matches('matcherB', has_entry(equal_to('b'), equal_to(2)), d)
        self.assert_does_not_match('matcherC', has_entry(equal_to('c'), equal_to(3)), d)

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        d = {'a': 1, 'b': 2}
        self.assert_matches('matcherA', has_entry('a', equal_to(1)), d)
        self.assert_matches('matcherB', has_entry(equal_to('b'), 2), d)
        self.assert_does_not_match('matcherC', has_entry('c', 3), d)

    def testHasReadableDescription(self):
        self.assert_description("dictionary containing ['a': <2>]",
                                has_entry('a', 2))

    def testMatchesQuasiDictionary(self):
        quasi = QuasiDictionary()
        self.assert_matches('quasi', has_entry(1, '1'), quasi)
        self.assert_does_not_match('other', has_entry(1, '1'), object())
        

if __name__ == '__main__':
    unittest.main()
