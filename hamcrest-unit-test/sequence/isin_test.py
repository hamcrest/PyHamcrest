if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.library.sequence.isin import is_in

from matcher_test import MatcherTest


class IsInTest(MatcherTest):

    def setUp(self):
        self.sequence = ('a', 'b', 'c')

    def testReturnsTrueIfArgumentIsInSequence(self):
        matcher = is_in(self.sequence)
        
        self.assert_matches('a', matcher, 'a')
        self.assert_matches('b', matcher, 'b')
        self.assert_matches('c', matcher, 'c')
        self.assert_does_not_match('d', matcher, 'd')

    def testHasReadableDescription(self):
        self.assert_description("one of ('a', 'b', 'c')", is_in(self.sequence))


if __name__ == '__main__':
    unittest.main()
