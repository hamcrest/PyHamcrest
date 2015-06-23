from __future__ import absolute_import

from hamcrest.library.collection.issequence_onlycontaining import *

from hamcrest.core.core.isequal import equal_to
from hamcrest.library.number.ordering_comparison import less_than
from hamcrest.library.object.haslength import has_length
from hamcrest_unit_test.matcher_test import MatcherTest
from .quasisequence import QuasiSequence
from .sequencemixin import SequenceForm, GeneratorForm
import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsSequenceOnlyContainingTestBase(object):

    def testMatchesSingletonList(self):
        self.assert_matches('singleton list', only_contains(equal_to(1)), self._sequence(1))

    def testMatchesAllItemsWithOneMatcher(self):
        self.assert_matches('one matcher',
                            only_contains(less_than(3)), self._sequence(0, 1, 2))

    def testMatchesAllItemsWithMultipleMatchers(self):
        self.assert_matches('multiple matchers',
                            only_contains(less_than(3), equal_to(7)),
                            self._sequence(0, 7, 1, 2))

    def testProvidesConvenientShortcutForMatchingWithEqualTo(self):
        self.assert_matches('Values automatically wrapped with equal_to',
                            only_contains(less_than(3), 7),
                            self._sequence(0, 7, 1, 2))

    def testDoesNotMatchListWithMismatchingItem(self):
        self.assert_does_not_match('3 is not less than 3',
                                   only_contains(less_than(3)), self._sequence(1, 2, 3))

    def testDoesNotMatchEmptyList(self):
        self.assert_does_not_match('empty', only_contains('foo'), self._sequence())

    def testMatchesAnyConformingSequence(self):
        class ObjectWithLenOnly(object):
            def __len__(self):
                return 20
            
        self.assert_matches('quasi-sequence',
                            only_contains(less_than(3)), QuasiSequence())
        self.assert_does_not_match('non-sequence', only_contains(1), object())
        self.assert_does_not_match('non-sequence with length',
                                   only_contains(1), ObjectWithLenOnly())

    def testHasAReadableDescription(self):
        self.assert_description('a sequence containing items matching (<1> or <2>)',
                                only_contains(1,2))

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
            "was 'bad', first sequence item not matching was 'b'", 
            only_contains(1,2), 'bad')

    def testDescribeMismatchDisplayUsedMatchersDescriptionForFirstFailingItem(self):
        has_length_matcher = has_length(1)
        has_length_description = 'an object with length of <1>'
        has_length_mismatch_text = "was 'sdf' with length of <3>"

        self.assert_description(has_length_description, has_length_matcher)
        self.assert_describe_mismatch(
            has_length_mismatch_text, has_length_matcher, 'sdf')

        sequence = self._sequence('a', 'sdf')
        prefix = postfix = ''
        if repr(sequence)[0] != '<':
            prefix = '<'
            postfix = '>'
        expected_only_contains_failure_text = \
            "was {prefix}{sequence!r}{postfix}, " \
            "first sequence item not matching {has_length_mismatch_text}".format(**locals())
        self.assert_describe_mismatch(
            expected_only_contains_failure_text,
            only_contains(has_length_matcher), sequence)

    def testDescribeMismatchOfNonSequence(self):
        self.assert_describe_mismatch("was <3>", only_contains(1,2), 3)


class IsConcreteSequenceOnlyContainingTest(MatcherTest, IsSequenceOnlyContainingTestBase, SequenceForm):
    pass

class IsGeneratorSequenceOnlyContainingTest(MatcherTest, IsSequenceOnlyContainingTestBase, GeneratorForm):
    pass


if __name__ == '__main__':
    unittest.main()
