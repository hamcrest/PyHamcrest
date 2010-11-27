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
from hamcrest.library.collection.isdict_containingkey import has_key

from matcher_test import MatcherTest
from quasidict import QuasiDictionary


class IsDictContainingKeyTest(MatcherTest):

    def testMatchesSingletonDictContainingKey(self):
        d = {'a': 1}
        self.assert_matches('Matches single key', has_key(equal_to('a')), d)

    def testMatchesDictContainingKey(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('Matches a', has_key(equal_to('a')), d)
        self.assert_matches('Matches c', has_key(equal_to('c')), d)

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('Matches c', has_key('c'), d)

    def testHasReadableDescription(self):
        self.assert_description("dictionary with key 'a'", has_key('a'))

    def testDoesNotMatchEmptyMap(self):
        self.assert_does_not_match('Empty dictionary', has_key('Foo'), {});

    def testDoesNotMatchMapMissingKey(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assert_does_not_match('Dictionary without matching key',
                                    has_key('d'), d)

    def testMatchesQuasiDictionary(self):
        self.assert_matches('quasi', has_key(1), QuasiDictionary())
        self.assert_does_not_match('other', has_key(1), object())


if __name__ == '__main__':
    unittest.main()
