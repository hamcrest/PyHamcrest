if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

from hamcrest.core.assert_raises import assert_raises
import unittest

__author__ = "Per Fagrell"
__copyright__ = "Copyright 2012 hamcrest.org"
__license__ = "BSD, see License.txt"


def doesNotThrowException():
    pass


class AssertRaisesTest(unittest.TestCase):
    def testShouldBeSilentIfRightExceptionRaised(self):
        self.function_called = False

        def throwsIoError():
            self.function_called = True
            raise ValueError()

        assert_raises(ValueError, throwsIoError)
        self.assertEqual(self.function_called, True)

    def testShouldRaiseAssertionErrorIfNoExceptionWasRaised(self):
        def doesNotThrow():
            pass

        try:
            assert_raises(ValueError, doesNotThrow)
        except AssertionError:
            return
        self.fail('should have failed')

    def testShouldRaiseAssertionErrorIfWrongExceptionTypeWasRaised(self):
        def throwsIoError():
            raise ValueError()

        try:
            assert_raises(KeyError, throwsIoError)
        except AssertionError:
            return
        self.fail('should have failed')

    def testAssertionErrorShouldDescribeExpectedAndActualExceptionTypes(self):
        expectedMessage = "\nExpected: ValueError raised\n     but: KeyError raised []\n"

        def throwsKeyError():
            raise KeyError()

        try:
            assert_raises(ValueError, throwsKeyError)
        except AssertionError, e:
            self.assertEqual(expectedMessage, str(e))
            return
        self.fail('should have failed')

    def testAssertionErrorShouldShowContentsOfActualException(self):
        expectedMessage = "\nExpected: ValueError raised\n     but: KeyError raised ['Index out of range']\n"

        def throwsKeyError():
            raise KeyError("Index out of range")

        try:
            assert_raises(ValueError, throwsKeyError)
        except AssertionError, e:
            self.assertEqual(expectedMessage, str(e))
            return
        self.fail('should have failed')


    def testAssertionErrorShouldDescribeExpectedException(self):
        expectedMessage = "\nExpected: ValueError raised\n     but: No exception raised\n"

        def doesNotThrow():
            pass

        try:
            assert_raises(ValueError, doesNotThrow)
        except AssertionError, e:
            self.assertEqual(expectedMessage, str(e))
            return
        self.fail('should have failed')
