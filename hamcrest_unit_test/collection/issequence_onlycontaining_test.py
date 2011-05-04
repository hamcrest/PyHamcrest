if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.collection.issequence_onlycontaining import *

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.number.ordering_comparison import less_than
from hamcrest_unit_test.matcher_test import MatcherTest
from quasisequence import QuasiSequence
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceOnlyContainingTest(MatcherTest):

    def testMatchesSingletonList(self):
        self.assert_matches('singleton list', only_contains(equal_to(1)), [1])

    def testMatchesAllItemsWithOneMatcher(self):
        self.assert_matches('one matcher',
                            only_contains(less_than(3)), [0, 1, 2])

    def testMatchesAllItemsWithMultipleMatchers(self):
        self.assert_matches('multiple matchers',
                            only_contains(less_than(3), equal_to(7)),
                            [0, 7, 1, 2])

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches('Values automatically wrapped with equal_to',
                            only_contains(less_than(3), 7),
                            [0, 7, 1, 2])

    def testDoesNotMatchListWithMismatchingItem(self):
        self.assert_does_not_match('3 is not less than 3',
                                   only_contains(less_than(3)), [1, 2, 3])

    def testDoesNotMatchEmptyList(self):
        self.assert_does_not_match('empty', only_contains('foo'), [])

    def testMatchesAnyConformingSequence(self):
        class ObjectWithLenOnly:
            def __len__(self): return 20
        self.assert_matches('quasi-sequence',
                            only_contains(less_than(3)), QuasiSequence())
        self.assert_does_not_match('non-sequence', only_contains(1), object())
        self.assert_does_not_match('non-sequence with length',
                                   only_contains(1), ObjectWithLenOnly())

    def testHasAReadableDescription(self):
        self.assert_description('a sequence containing items matching (<1> or <2>)',
                                only_contains(1,2))

    def testDescribeMismatch(self):
        self.assert_describe_mismatch("was 'bad'", only_contains(1,2), 'bad')

    def testDescribeMismatchOfNonSequence(self):
        self.assert_describe_mismatch("was <3>", only_contains(1,2), 3)


if __name__ == '__main__':
    unittest.main()
