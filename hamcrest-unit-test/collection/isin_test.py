__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.library.collection.isin import is_in

from matcher_test import MatcherTest


sequence = ('a', 'b', 'c')

class IsInTest(MatcherTest):

    def testReturnsTrueIfArgumentIsInSequence(self):
        matcher = is_in(sequence)

        self.assert_matches('a', matcher, 'a')
        self.assert_matches('b', matcher, 'b')
        self.assert_matches('c', matcher, 'c')
        self.assert_does_not_match('d', matcher, 'd')

    def testHasReadableDescription(self):
        self.assert_description("one of ('a', 'b', 'c')", is_in(sequence))


if __name__ == '__main__':
    unittest.main()
