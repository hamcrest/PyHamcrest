__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class IsEqualTest(MatcherTest):

    def testComparesObjectsUsingEquality(self):
        assert_that('hi', equal_to('hi'))
        assert_that('bye', is_not(equal_to('hi')))

        assert_that(1, equal_to(1))
        assert_that(1, is_not(equal_to(2)))

    def testCanCompareNoneValues(self):
        assert_that(None, equal_to(None));

        assert_that(None, is_not(equal_to("hi")));
        assert_that("hi", is_not(equal_to(None)));

    def testHonoursEqImplementation(self):
        class AlwaysEqual:
            def __eq__(self, obj): return True
        class NeverEqual:
            def __eq__(self, obj): return False
        assert_that(AlwaysEqual(), equal_to(1));
        assert_that(NeverEqual(), is_not(equal_to(1)));

    def testIncludesTheResultOfCallingToStringOnItsArgumentInTheDescription(self):
        argument_description = 'ARGUMENT DESCRIPTION'
        class Argument:
            def __str__(self): return argument_description
        self.assert_description('<' + argument_description + '>', equal_to(Argument()))

    def testReturnsAnObviousDescriptionIfCreatedWithANestedMatcherByMistake(self):
        inner_matcher = equal_to('NestedMatcher')
        self.assert_description('<' + str(inner_matcher) + '>', equal_to(inner_matcher))


if __name__ == '__main__':
    unittest.main()
