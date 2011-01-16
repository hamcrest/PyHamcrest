__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.is_ import is_

from matcher_test import MatcherTest


class FakeMatcher(BaseMatcher):

    def matches(self, item, mismatch_description=None):
        self.describe_mismatch(item, mismatch_description)
        return False

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('MISMATCH')

#------------------------------------------------------------------------------

class IsTest(MatcherTest):

    def testJustMatchesTheSameWayTheUnderylingMatcherDoes(self):
        self.assert_matches('should match', is_(equal_to(True)), True)
        self.assert_matches('should match', is_(equal_to(False)), False)
        self.assert_does_not_match('should not match', is_(equal_to(True)), False)
        self.assert_does_not_match('should not match', is_(equal_to(False)), True)

    def testGeneratesIsPrefixInDescription(self):
        self.assert_description('is <True>', is_(equal_to(True)))

    def testProvidesConvenientShortcutForIsEqualTo(self):
        self.assert_matches('should match', is_('A'), 'A');
        self.assert_matches('should match', is_('B'), 'B');
        self.assert_does_not_match('should not match', is_('A'), 'B');
        self.assert_does_not_match('should not match', is_('B'), 'A');
        self.assert_description("is 'A'", is_('A'));

    def testProvidesConvenientShortcutForIsInstanceOf(self):
        self.assert_matches('should match', is_(str), 'A');
        self.assert_does_not_match('should not match', is_(int), 'A');

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(is_('A'), 'A')

    def testMismatchDescriptionUsesNestedMatcherToDescribeMismatch(self):
        self.assert_mismatch_description(
                                "MISMATCH",
                                is_(FakeMatcher()),
                                'hi')

    def testDescribeMismatch(self):
        self.assert_describe_mismatch(
                                "MISMATCH",
                                is_(FakeMatcher()),
                                'hi')


if __name__ == '__main__':
    unittest.main()
