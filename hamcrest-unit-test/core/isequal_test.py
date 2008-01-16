if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isequal import equalto
from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class FakeArgument:
    def __str__(self):
        return 'ARGUMENT DESCRIPTION'


class IsEqualTest(MatcherTest):

    def testComparesObjectsUsingEquality(self):
        assert_that('hi', equalto('hi'))
        assert_that('bye', not_(equalto('hi')))

        assert_that(1, equalto(1))
        assert_that(1, not_(equalto(2)))

    def testIncludesTheResultOfCallingToStringOnItsArgumentInTheDescription(self):
        self.assert_description('<ARGUMENT DESCRIPTION>', equalto(FakeArgument()))

    def testReturnsAnObviousDescriptionIfCreatedWithANestedMatcherByMistake(self):
        inner_matcher = equalto('NestedMatcher')
        self.assert_description('<' + str(inner_matcher) + '>', equalto(inner_matcher))


if __name__ == '__main__':
    unittest.main()
