if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that
from hamcrest.core.string_description import tostring
from hamcrest.library.object.hasstring import has_string

from matcher_test import MatcherTest


STR_RESULT = 'str result'

class HasStringTest(MatcherTest):

    def testPassesResultOfToStringToNestedMatcher(self):
        class FakeObject:
            def __str__(self): return STR_RESULT
        ARG = FakeObject()
        assert_that(ARG, has_string(equal_to(STR_RESULT)))
        assert_that(ARG, is_not(has_string(equal_to('OTHER STRING'))))

    def testHasReadableDescription(self):
        string_matcher = equal_to(STR_RESULT)
        matcher = has_string(string_matcher)

        self.assertEquals('str(' + _descriptionof(string_matcher) + ')',
                        _descriptionof(matcher))


def _descriptionof(matcher):
    return tostring(matcher);


if __name__ == '__main__':
    unittest.main()
