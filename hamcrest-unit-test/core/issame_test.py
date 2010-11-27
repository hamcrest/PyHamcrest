__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest
import re

from hamcrest.core.core.issame import same_instance
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.core.string_description import StringDescription

from matcher_test import MatcherTest


class IsSameTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsReferenceToASpecifiedObject(self):
        o1 = object()
        o2 = object()

        assert_that(o1, same_instance(o1))
        assert_that(o2, is_not(same_instance(o1)))

    def testHasAReadableDescription(self):
        self.assert_description("same_instance('ARG')", same_instance('ARG'))

    def testDescribeMismatch(self):
        o1 = object()
        o2 = object()
        matcher = same_instance(o1)
        description = StringDescription()

        matcher.describe_mismatch(o2, description)
        expected = re.compile('was <<object object at 0x[0-9a-fA-F]+>> with id [0-9]+')
        self.assert_(expected.match(str(description)))


if __name__ == '__main__':
    unittest.main()
