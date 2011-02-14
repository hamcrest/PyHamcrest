__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.collection.issequence_containinginorder import *

from hamcrest.core.core.isequal import equal_to
from matcher_test import MatcherTest
from quasisequence import QuasiSequence
import unittest


class IsSequenceContainingInOrderTest(MatcherTest):

    def testMatchingSingleItemSequence(self):
        self.assert_matches("Single item sequence", contains(equal_to(1)), [1])

    def testMatchingMultipleItemSequence(self):
        self.assert_matches("Multiple item sequence",
                            contains(equal_to(1), equal_to(2), equal_to(3)),
                            [1,2,3])

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        self.assert_matches("Values automatically wrapped with equal_to",
                            contains(1, 2, 3),
                            [1,2,3])

    def testDoesNotMatchWithMoreElementsThanExpected(self):
        self.assert_mismatch_description("Not matched: <4>",
                            contains(1,2,3), [1,2,3,4])

    def testDoesNotMatchWithFewerElementsThanExpected(self):
        self.assert_mismatch_description("No item matched: <3>",
                            contains(1,2,3), [1,2])

    def testDoesNotMatchIfSingleItemMismatches(self):
        self.assert_mismatch_description("item 0: was <3>", contains(4), [3])

    def testDoesNotMatchIfOneOfMultipleItemsMismatch(self):
        self.assert_mismatch_description("item 2: was <4>",
                            contains(1,2,3), [1,2,4])

    def testDoesNotMatchEmptySequence(self):
        self.assert_mismatch_description("No item matched: <4>",
                            contains(4), [])

    def testEmptySequenceMatchesEmptySequence(self):
        self.assert_matches("Empty sequence", contains(), [])

    def testMatchesAnyConformingSequence(self):
        self.assert_matches('quasi-sequence', contains(1,2), QuasiSequence())
        self.assert_does_not_match('non-sequence', contains(1,2), object())

    def testHasAReadableDescription(self):
        self.assert_description("a sequence containing [<1>, <2>]", contains(1,2))

    def testDescribeMismatch(self):
        self.assert_describe_mismatch('item 1: was <3>', contains(1,2), [1,3])

    def testDescribeMismatchOfNonSequence(self):
        self.assert_describe_mismatch("was <3>", contains(1,2), 3)

if __name__ == '__main__':
    unittest.main()
