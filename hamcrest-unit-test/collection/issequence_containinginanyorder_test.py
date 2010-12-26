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
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder

from matcher_test import MatcherTest
from quasisequence import QuasiSequence


class IsSequenceContainingInAnyOrderTest(MatcherTest):

    def testMatchingSingleItemSequence(self):
        self.assert_matches("Single item sequence",
                            contains_inanyorder(equal_to(1)), [1])

    def testDoesNotMatchEmptySequence(self):
        self.assert_mismatch_description("No item matches: <1>, <2> in []",
                            contains_inanyorder(1, 2), [])

    def testEmptySequenceMatchesEmptySequence(self):
        self.assert_matches("Empty sequence", contains_inanyorder(), [])

    def testMatchesSequenceOutOfOrder(self):
        self.assert_matches("Out of order",
                            contains_inanyorder(equal_to(1), equal_to(2)),
                            [2,1])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches("Values automatically wrapped with equal_to",
                            contains_inanyorder(1,2),
                            [2,1])

    def testMatchesSequenceInOrder(self):
        self.assert_matches("In order", contains_inanyorder(1,2), [1,2])

    def testDoesNotMatchIfOneOfMultipleItemsMismatch(self):
        self.assert_mismatch_description("Not matched: <4>",
                            contains_inanyorder(1,2,3), [1,2,4])

    def testDoesNotMatchWithMoreElementsThanExpected(self):
        self.assert_mismatch_description("Not matched: <2>",
                            contains_inanyorder(1,3), [1,2,3])

    def testDoesNotMatchWithFewerElementsThanExpected(self):
        self.assert_mismatch_description(
                            "No item matches: <4> in [<1>, <2>, <3>]",
                            contains_inanyorder(1,2,3,4), [1,2,3])

    def testDescribeMismatch(self):
        self.assert_describe_mismatch('Not matched: <3>',
                            contains_inanyorder(1,2), [1,3])

    def testHasAReadableDescription(self):
        self.assert_description("sequence over [<1>, <2>] in any order",
                                contains_inanyorder(1,2))

    def testMatchesAnyConformingSequence(self):
        self.assert_matches('quasi-sequence', contains_inanyorder(1,2),
                            QuasiSequence())
        self.assert_does_not_match('non-sequence', contains_inanyorder(1,2),
                            object())


if __name__ == '__main__':
    unittest.main()
