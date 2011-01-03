__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

import unittest

from hamcrest.core.core.isequal import equal_to
from hamcrest.core.matcher_assert import assert_that


class MatcherAssertTest(unittest.TestCase):

    def testIncludesDescriptionOfTestedValueInErrorMessage(self):
        expected = 'expected'
        actual = 'actual'

        expectedMessage = "identifier\nExpected: 'expected'\n     but: was 'actual'\n"

        try:
            assert_that(actual, equal_to(expected), 'identifier')
        except AssertionError, e:
            self.assertEquals(expectedMessage, str(e))
            return

        self.fail('should have failed')

    def testDescriptionCanBeElided(self):
        expected = 'expected'
        actual = 'actual'

        expectedMessage = "\nExpected: 'expected'\n     but: was 'actual'\n"

        try:
            assert_that(actual, equal_to(expected))
        except AssertionError, e:
            self.assertEquals(expectedMessage, str(e))
            return

        self.fail('should have failed')

    def testCanTestBoolDirectly(self):
        assert_that(True, 'success reason message')

        try:
            assert_that(False, 'failing reason message')
        except AssertionError, e:
            self.assertEquals('failing reason message', str(e))
            return

        self.fail('should have failed')


if __name__ == "__main__":
    unittest.main()
