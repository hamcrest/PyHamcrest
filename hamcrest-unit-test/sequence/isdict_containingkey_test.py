if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.library.sequence.isdict_containingkey import haskey

from matcher_test import MatcherTest
from quasidict import QuasiDictionary


class IsDictContainingKeyTest(MatcherTest):

    def testMatchesSingletonDictContainingKey(self):
        d = {'a': 1}
        self.assert_matches('Matches single key', haskey(equalto('a')), d)

    def testMatchesDictContainingKey(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('Matches a', haskey(equalto('a')), d)
        self.assert_matches('Matches c', haskey(equalto('c')), d)

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('Matches c', haskey('c'), d)

    def testHasReadableDescription(self):
        self.assert_description("dictionary with key 'a'", haskey('a'))

    def testDoesNotMatchEmptyMap(self):
        self.assert_does_not_match('Empty dictionary', haskey('Foo'), {});

    def testDoesNotMatchMapMissingKey(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_does_not_match('Dictionary without matching key',
                                    haskey('d'), d)

    def testMatchesQuasiDictionary(self):
        quasi = QuasiDictionary()
        self.assert_matches('quasi', haskey(1), quasi)
        self.assert_does_not_match('other', haskey(1), object())


if __name__ == '__main__':
    unittest.main()
