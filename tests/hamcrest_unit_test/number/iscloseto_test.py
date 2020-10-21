import unittest

from hamcrest.library.number.iscloseto import Decimal, close_to, isnumeric
from hamcrest_unit_test.matcher_test import MatcherTest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsCloseToTest(MatcherTest):
    def testEvaluatesToTrueIfArgumentIsEqualToAValueWithinSomeError(self):
        matcher = close_to(1.0, 0.5)

        self.assert_matches("equal", matcher, 1.0)
        self.assert_matches("less but within delta", matcher, 0.5)
        self.assert_matches("greater but within delta", matcher, 1.5)

        self.assert_does_not_match("too small", matcher, 0.4)
        self.assert_does_not_match("too large", matcher, 1.6)

    def testMatcherCreationAcceptsOtherNumericTypes(self):
        close_to(int(5), int(1))

    def testMatcherCreationRequiresNumbers(self):
        self.assertRaises(TypeError, close_to, "a", 0.5)
        self.assertRaises(TypeError, close_to, 1.0, "a")

    def testFailsIfMatchingAgainstNonNumber(self):
        self.assert_does_not_match("not a number", close_to(1.0, 0.5), "a")

    def testHasAReadableDescription(self):
        self.assert_description("a numeric value within <0.5> of <1.0>", close_to(1.0, 0.5))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(close_to(1.0, 0.5), 1.0)

    def testMismatchDescriptionShowsActualDeltaIfArgumentIsNumeric(self):
        self.assert_mismatch_description("<1.7> differed by <0.7>", close_to(1.0, 0.5), 1.7)

    def testMismatchDescriptionShowsActualArgumentIfNotNumeric(self):
        self.assert_mismatch_description("was 'bad'", close_to(1.0, 0.5), "bad")

    def testDescribeMismatchShowsActualDeltaIfArgumentIsNumeric(self):
        self.assert_describe_mismatch("<1.7> differed by <0.7>", close_to(1.0, 0.5), 1.7)

    def testDescribeMismatchShowsActualArgumentIfNotNumeric(self):
        self.assert_describe_mismatch("was 'bad'", close_to(1.0, 0.5), "bad")

    def testMatcherSupportsDecimal(self):
        matcher = close_to(Decimal("1.0"), Decimal("0.5"))

        self.assert_matches("equal", matcher, Decimal("1.4"))


try:
    import numpy as np

    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False


class IsNumericTest(unittest.TestCase):
    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_int(self):
        self.assertTrue(isnumeric(np.int(1)), "Platform integer (normally either int32 or int64)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_int8(self):
        self.assertTrue(isnumeric(np.int8(1)), "Byte (-128 to 127)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_int16(self):
        self.assertTrue(isnumeric(np.int16(1)), "Integer (-32768 to 32767)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_int32(self):
        self.assertTrue(isnumeric(np.int32(1)), "Integer (-2147483648 to 2147483647)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_int64(self):
        self.assertTrue(
            isnumeric(np.int64(1)), "Integer (9223372036854775808 to 9223372036854775807)"
        )

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_uint8(self):
        self.assertTrue(isnumeric(np.uint8(1)), "Unsigned integer (0 to 255)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_uint16(self):
        self.assertTrue(isnumeric(np.uint16(1)), "Unsigned integer (0 to 65535)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_uint32(self):
        self.assertTrue(isnumeric(np.uint32(1)), "Unsigned integer (0 to 4294967295)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_uint64(self):
        self.assertTrue(isnumeric(np.uint64(1)), "Unsigned integer (0 to 18446744073709551615)")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_float(self):
        self.assertTrue(isnumeric(np.float(1)), "Shorthand for float64.")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_float16(self):
        self.assertTrue(
            isnumeric(np.float16(1)),
            "Half precision float: sign bit, 5 bits exponent, 10 bits mantissa",
        )

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_float32(self):
        self.assertTrue(
            isnumeric(np.float32(1)),
            "Single precision float: sign bit, 8 bits exponent, 23 bits mantissa",
        )

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_float64(self):
        self.assertTrue(
            isnumeric(np.float64(1)),
            "Double precision float: sign bit, 11 bits exponent, 52 bits mantissa",
        )

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_complex(self):
        self.assertTrue(isnumeric(np.complex(1)), "Shorthand for complex128.")

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_complex64(self):
        self.assertTrue(
            isnumeric(np.complex64(1)),
            "Complex number, represented by two 32-bit floats (real and imaginary components)",
        )

    @unittest.skipUnless(NUMPY_AVAILABLE, "Skipped because it needs NumPy")
    def test_numpy_numeric_type_complex128(self):
        self.assertTrue(
            isnumeric(np.complex128(1)),
            "Complex number, represented by two 64-bit floats (real and imaginary components)",
        )


if __name__ == "__main__":
    unittest.main()
