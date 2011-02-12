__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
import unittest


class AssertThatTest(unittest.TestCase):

    def testShouldBeSilentOnSuccessfulMatch(self):
        assert_that(1, equal_to(1))

    def testAssertionErrorShouldDescribeExpectedAndActual(self):
        expected = 'EXPECTED'
        actual = 'ACTUAL'

        expectedMessage = "\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        try:
            assert_that(actual, equal_to(expected))
        except AssertionError, e:
            self.assertEqual(expectedMessage, str(e))
            return
        self.fail('should have failed')

    def testAssertionErrorShouldIncludeOptionalReason(self):
        expected = 'EXPECTED'
        actual = 'ACTUAL'

        expectedMessage = "REASON\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        try:
            assert_that(actual, equal_to(expected), 'REASON')
        except AssertionError, e:
            self.assertEqual(expectedMessage, str(e))
            return
        self.fail('should have failed')

    def testCanTestBoolDirectly(self):
        assert_that(True, 'should accept True')

        try:
            assert_that(False, 'FAILURE REASON')
        except AssertionError, e:
            self.assertEqual('FAILURE REASON', str(e))
            return

        self.fail('should have failed')

    def testCanTestBoolDirectlyWithoutReason(self):
        assert_that(True)

        try:
            assert_that(False)
        except AssertionError, e:
            self.assertEqual('Assertion failed', str(e))
            return

        self.fail('should have failed')


if __name__ == "__main__":
    unittest.main()
