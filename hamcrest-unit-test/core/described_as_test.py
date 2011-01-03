__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.described_as import described_as
from hamcrest.core.core.isanything import anything
from hamcrest.core.core.isnot import is_not

from matcher_test import MatcherTest


class DescribedAsTest(MatcherTest):

    def testOverridesDescriptionOfOtherMatcherWithThatPassedToConstructor(self):
        m1 = described_as('m1 description', anything())
        m2 = described_as('m2 description', is_not(anything()))

        self.assert_description('m1 description', m1)
        self.assert_description('m2 description', m2)

    def testAppendsValuesToDescription(self):
        m = described_as('value 1 = %0, value 2 = %1', anything(), 33, 97)

        self.assert_description('value 1 = <33>, value 2 = <97>', m)

    def testDelegatesMatchingToAnotherMatcher(self):
        m1 = described_as('irrelevant', anything())
        m2 = described_as('irrelevant', is_not(anything()))

        self.assert_(m1.matches(object()))
        self.assert_(not m2.matches('hi'))


if __name__ == '__main__':
    unittest.main()
