if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.issame import same_instance
from hamcrest.core.core.isnot import is_not
from hamcrest.core.matcher_assert import assert_that

from matcher_test import MatcherTest


class IsSameTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentIsReferenceToASpecifiedObject(self):
        o1 = object()
        o2 = object()
        
        assert_that(o1, same_instance(o1))
        assert_that(o2, is_not(same_instance(o1)))

    def testHasAReadableDescription(self):
        self.assert_description("same_instance('ARG')", same_instance('ARG'))


if __name__ == '__main__':
    unittest.main()
