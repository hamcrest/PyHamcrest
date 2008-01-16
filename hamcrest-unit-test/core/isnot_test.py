if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.isnot import not_

from matcher_test import MatcherTest


class IsNotTest(MatcherTest):

    def testEvaluatesToTheTheLogicalNegationOfAnotherMatcher(self):
        self.assert_matches('should match', not_(equalto('A')), 'B')
        self.assert_does_not_match('should not match', not_(equalto('B')), 'B')

    def testProvidesConvenientShortcutForNotEqualTo(self):
        self.assert_matches('should match', not_('A'), 'B');
        self.assert_matches('should match', not_('B'), 'A');
        self.assert_does_not_match('should not match', not_('A'), 'A');
        self.assert_does_not_match('should not match', not_('B'), 'B');
    
    def testHasAReadableDescription(self):
        self.assert_description("not 'A'", not_('A'));


if __name__ == '__main__':
    unittest.main()
