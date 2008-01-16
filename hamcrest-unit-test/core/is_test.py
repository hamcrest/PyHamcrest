if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.is_ import is_

from matcher_test import MatcherTest


class IsTest(MatcherTest):

    def testJustMatchesTheSameWayTheUnderylingMatcherDoes(self):
        self.assert_matches('should match', is_(equalto(True)), True)
        self.assert_matches('should match', is_(equalto(False)), False)
        self.assert_does_not_match('should not match', is_(equalto(True)), False)
        self.assert_does_not_match('should not match', is_(equalto(False)), True)

    def testGeneratesIsPrefixInDescription(self):
        self.assert_description('is <True>', is_(equalto(True)))

    def testProvidesConvenientShortcutForIsEqualTo(self):
        self.assert_matches('should match', is_('A'), 'A');
        self.assert_matches('should match', is_('B'), 'B');
        self.assert_does_not_match('should not match', is_('A'), 'B');
        self.assert_does_not_match('should not match', is_('B'), 'A');
        self.assert_description("is 'A'", is_('A'));

    def testProvidesConvenientShortcutForIsInstanceOf(self):
        self.assert_matches('should match', is_(str), 'A');
        self.assert_does_not_match('should not match', is_(int), 'A');


if __name__ == '__main__':
    unittest.main()
