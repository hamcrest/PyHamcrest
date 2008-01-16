if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.library.sequence.isdict_containing import hasentry

from matcher_test import MatcherTest
from quasidict import QuasiDictionary


class IsDictContainingTest(MatcherTest):

    def testMatchesDictContainingMatchingKeyAndValue(self):
        d = {'a': 1, 'b': 2}
        self.assert_matches('matcherA', hasentry(equalto('a'), equalto(1)), d)
        self.assert_matches('matcherB', hasentry(equalto('b'), equalto(2)), d)
        self.assert_does_not_match('matcherC', hasentry(equalto('c'), equalto(3)), d)

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        d = {'a': 1, 'b': 2}
        self.assert_matches('matcherA', hasentry('a', equalto(1)), d)
        self.assert_matches('matcherB', hasentry(equalto('b'), 2), d)
        self.assert_does_not_match('matcherC', hasentry('c', 3), d)

    def testHasReadableDescription(self):
        self.assert_description("dictionary containing ['a': <2>]",
                                hasentry('a', 2))

    def testMatchesQuasiDictionary(self):
        quasi = QuasiDictionary()
        self.assert_matches('quasi', hasentry(1, '1'), quasi)
        self.assert_does_not_match('other', hasentry(1, '1'), object())
        

if __name__ == '__main__':
    unittest.main()
