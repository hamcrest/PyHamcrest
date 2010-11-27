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
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.object.hasstring import has_string

from matcher_test import MatcherTest


str_result = 'str result'

class FakeObject:
    def __str__(self): return str_result


class HasStringTest(MatcherTest):

    def testPassesResultOfToStrToNestedMatcher(self):
        object = FakeObject()
        assert_that(object, has_string(equal_to(str_result)))
        assert_that(object, is_not(has_string(equal_to('other'))))

    def testProvidesConvenientShortcutForHasStringEqualTo(self):
        object = FakeObject()
        assert_that(object, has_string(str_result))
        assert_that(object, is_not(has_string('other')))

    def testHasReadableDescription(self):
        string_matcher = equal_to(str_result)
        matcher = has_string(string_matcher)
        self.assertEquals('str(' + str(string_matcher) + ')', str(matcher))


if __name__ == '__main__':
    unittest.main()
