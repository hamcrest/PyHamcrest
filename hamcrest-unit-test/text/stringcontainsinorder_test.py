if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.text.stringcontainsinorder import *

from hamcrest.core.string_description import StringDescription
from matcher_test import MatcherTest
import unittest

__author__ = "Romilly Cocking"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class StringContainsInOrderTest(MatcherTest):
    def setUp(self):
        self. matcher = StringContainsInOrder('string one','string two','string three')

    def testMatchesIfOrderIsCorrect(self):
        self.assertTrue(self.matcher.matches('string one then string two followed by string three'),'correct order')

    def testDoesNotMatchIfOrderIsIncorrect(self):
        self.assertFalse(self.matcher.matches('string two then string one followed by string three'),'incorrect order')

    def testDoesNotMatchIfExpectedSubstringsAreMissing(self):
        self.assertFalse(self.matcher.matches('string two then string three'),'missing string one')
        self.assertFalse(self.matcher.matches('string one then string three'),'missing string two')
        self.assertFalse(self.matcher.matches('string one then string two'),'missing string three')

    def testDescribesSelf(self):
        description = StringDescription()
        self.matcher.describe_to(description)
        self.assertEqual("a string containing 'string one', 'string two', 'string three' in order", str(description))

    def testMismatchDescription(self):
        description = StringDescription()
        self.matcher.describe_mismatch('foo', description)
        self.assertEqual("was 'foo'", str(description))
