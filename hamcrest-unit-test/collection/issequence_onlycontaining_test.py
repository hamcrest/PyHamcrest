if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.issequence_onlycontaining import only_contains
from hamcrest.library.number.ordering_comparison import less_than

from matcher_test import MatcherTest
from quasisequence import QuasiSequence


class IsSequenceOnlyContainingTest(MatcherTest):

    def testDoesNotMatchEmptyList(self):
        self.assert_does_not_match('empty sequence',
                                    only_contains(equal_to('foo')), [])

    def testMatchesSingletonList(self):
        self.assert_matches('singleton list',
                            only_contains(equal_to(1)), [1])

    def testMatchesList(self):
        self.assert_matches('list',
                            only_contains(equal_to(1), equal_to(2), equal_to(3)),
                            [1, 2, 3])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches('list',
                            only_contains(1, equal_to(2), 3),
                            [1, 2, 3])

    def testDoesNotMatchListWithMismatchingItem(self):
        self.assert_does_not_match('list',
                            only_contains(1, 2),
                            [1, 2, 3])

    def testHasAReadableDescription(self):
        self.assert_description('a sequence containing items matching (<1> or <2>)',
                            only_contains(1, 2))

    def testMatchesQuasiSequence(self):
        class ObjectWithLenOnly:
            def __len__(self): return 20
        self.assert_matches('quasi', only_contains(less_than(3)), QuasiSequence())
        self.assert_does_not_match('other', only_contains(1), object())
        self.assert_does_not_match('other', only_contains(1), ObjectWithLenOnly())


if __name__ == '__main__':
    unittest.main()
