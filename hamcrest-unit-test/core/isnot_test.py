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
from hamcrest.core.core.isnot import is_not

from matcher_test import MatcherTest


class IsNotTest(MatcherTest):

    def testEvaluatesToTheTheLogicalNegationOfAnotherMatcher(self):
        self.assert_matches('should match', is_not(equal_to('A')), 'B')
        self.assert_does_not_match('should not match', is_not(equal_to('B')), 'B')

    def testProvidesConvenientShortcutForNotEqualTo(self):
        self.assert_matches('should match', is_not('A'), 'B');
        self.assert_matches('should match', is_not('B'), 'A');
        self.assert_does_not_match('should not match', is_not('A'), 'A');
        self.assert_does_not_match('should not match', is_not('B'), 'B');

    def testHasAReadableDescription(self):
        self.assert_description("not 'A'", is_not('A'));


if __name__ == '__main__':
    unittest.main()
