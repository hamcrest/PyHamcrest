if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.core.string_description import tostring
from hamcrest.library.object.hasstring import hasstring

from matcher_test import MatcherTest


STR_RESULT = 'str result'

class FakeObject:
    def __str__(self):
        return STR_RESULT


class HasStringTest(MatcherTest):

    def testPassesResultOfToStringToNestedMatcher(self):
        ARG = FakeObject()
        assert_that(ARG, hasstring(equalto(STR_RESULT)))
        assert_that(ARG, not_(hasstring(equalto('OTHER STRING'))))

    def testHasReadableDescription(self):
        string_matcher = equalto(STR_RESULT)
        matcher = hasstring(string_matcher)

        self.assertEquals('str(' + _descriptionof(string_matcher) + ')', _descriptionof(matcher))


def _descriptionof(matcher):
    return tostring(matcher);


if __name__ == '__main__':
    unittest.main()
