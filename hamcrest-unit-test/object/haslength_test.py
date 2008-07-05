if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.object.haslength import has_length

from matcher_test import MatcherTest


len_result = 42

class FakeObject:
    def __len__(self): return len_result


class HasStringTest(MatcherTest):

    def testPassesResultOfLenToNestedMatcher(self):
        object = FakeObject()
        assert_that(object, has_length(equal_to(len_result)))
        assert_that(object, is_not(has_length(equal_to(1))))

    def testProvidesConvenientShortcutForHasLengthEqualTo(self):
        object = FakeObject()
        assert_that(object, has_length(len_result))
        assert_that(object, is_not(has_length(1)))

    def testDoesNotMatchObjectWithoutLen(self):
        assert_that(object(), is_not(has_length(equal_to(1))))

    def testHasReadableDescription(self):
        length_matcher = equal_to(len_result)
        matcher = has_length(length_matcher)
        self.assertEquals('len(' + str(length_matcher) + ')', str(matcher))


if __name__ == '__main__':
    unittest.main()
