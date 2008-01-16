if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.library.number.ordering_comparison import lessthan
from hamcrest.library.sequence.issequence_onlycontaining import onlycontains

from matcher_test import MatcherTest
from quasisequence import QuasiSequence


class ObjectWithLenOnly:
    def __len__(self):
        return 20


class IsSequenceOnlyContainingTest(MatcherTest):

    def testDoesNotMatchEmptyArray(self):
        self.assert_does_not_match('empty sequence',
                                    onlycontains(equalto('foo')), [])

    def testMatchesSingletonList(self):
        self.assert_matches('singleton list',
                            onlycontains(equalto(1)), [1])

    def testMatchesList(self):
        self.assert_matches('list',
                            onlycontains(equalto(1), equalto(2), equalto(3)),
                            [1, 2, 3])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches('list',
                            onlycontains(1, equalto(2), 3),
                            [1, 2, 3])

    def testMatchesQuasiSequence(self):
        quasi = QuasiSequence()
        self.assert_matches('quasi', onlycontains(lessthan(3)), quasi)
        self.assert_does_not_match('other', onlycontains(1), object())
        self.assert_does_not_match('other', onlycontains(1),
                                    ObjectWithLenOnly())


if __name__ == '__main__':
    unittest.main()
