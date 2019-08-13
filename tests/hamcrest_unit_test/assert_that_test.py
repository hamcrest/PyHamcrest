# encoding: utf-8
import unittest
import warnings

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to


def u(x):
    return x


__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AssertThatTest(unittest.TestCase):
    def testShouldBeSilentOnSuccessfulMatch(self):
        assert_that(1, equal_to(1))

    def testAssertionErrorShouldDescribeExpectedAndActual(self):
        expected = "EXPECTED"
        actual = "ACTUAL"

        expectedMessage = "\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        with self.assertRaises(AssertionError) as e:
            assert_that(actual, equal_to(expected))

        self.assertEqual(expectedMessage, str(e.exception))

    def testAssertionErrorShouldIncludeOptionalReason(self):
        expected = "EXPECTED"
        actual = "ACTUAL"

        expectedMessage = "REASON\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        with self.assertRaises(AssertionError) as e:
            assert_that(actual, equal_to(expected), "REASON")

        self.assertEqual(expectedMessage, str(e.exception))

    def testAssertionUnicodeEncodesProperly(self):
        expected = "EXPECTED"
        actual = u("\xdcnic\N{Latin Small Letter O with diaeresis}de")

        with self.assertRaises(AssertionError):
            assert_that(actual, equal_to(expected), "REASON")

    def testCanTestBoolDirectly(self):
        assert_that(True, "should accept True")

        with self.assertRaises(AssertionError) as e:
            assert_that(False, "FAILURE REASON")
        self.assertEqual("FAILURE REASON", str(e.exception))

    def testCanTestBoolDirectlyWithoutReason(self):
        assert_that(True)

        with self.assertRaises(AssertionError) as e:
            assert_that(False)

        self.assertEqual("Assertion failed", str(e.exception))

    def testWarnsForMatcherAsArg1(self):
        assert_that(True)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            assert_that(equal_to(1))

            self.assertEqual(len(w), 1)
            self.assertTrue("arg1 should be boolean" in str(w[-1].message))


if __name__ == "__main__":
    unittest.main()
