# encoding: utf-8
import unittest

from hamcrest.core.assert_that import DeferAssertContextManager
from hamcrest.core.core.isequal import equal_to


class DeferAssertContextManagerTest(unittest.TestCase):
    def testAssertionSuccessfully(self):
        with DeferAssertContextManager() as da:
            da.assert_that(1, equal_to(1))

    def testAssertionTeardownSuccessfully(self):
        actual = "ACTUAL"

        with DeferAssertContextManager() as da:
            da.assert_that(actual, equal_to("ACTUAL"))
            actual = ""
        self.assertEqual(actual, "")

    def testAssertionErrorShouldTeardownBeforeRaiseExeption(self):
        self.maxDiff = None
        expected = "EXPECTED"
        actual = "ACTUAL"

        expectedMessage = "\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        with self.assertRaises(AssertionError) as e:
            with DeferAssertContextManager() as da:
                da.assert_that(actual, equal_to(expected))
                actual = ""
        self.assertEqual(actual, "")
        self.assertEqual(expectedMessage, str(e.exception))

    def testAssertionErrorShouldRaiseExceptionBeforeExitingContext(self):
        self.maxDiff = None
        expected = "EXPECTED"
        actual = "ACTUAL"

        expectedMessage = "\nExpected: 'EXPECTED'\n     but: was 'ACTUAL'\n"

        with self.assertRaises(AssertionError) as e:
            with DeferAssertContextManager() as da:
                da.assert_that(actual, equal_to(expected))
            actual = ""
        self.assertNotEqual(actual, "")
        self.assertEqual(expectedMessage, str(e.exception))


if __name__ == "__main__":
    unittest.main()
