import sys
import unittest

import pytest
from hamcrest import has_properties, not_
from hamcrest.core.core.raises import calling, raises
from hamcrest_unit_test.matcher_test import MatcherTest, assert_mismatch_description

if __name__ == "__main__":
    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")


__author__ = "Per Fagrell"
__copyright__ = "Copyright 2013 hamcrest.org"
__license__ = "BSD, see License.txt"


def no_exception(*args, **kwargs):
    return


def raise_exception(*args, **kwargs):
    raise AssertionError(str(args) + str(kwargs))


def raise_baseException(*args, **kwargs):
    raise SystemExit(str(args) + str(kwargs))


def raise_exception_with_properties(**kwargs):
    err = AssertionError("boom")
    for k, v in kwargs.items():
        setattr(err, k, v)
    raise err


class RaisesTest(MatcherTest):
    def testMatchesIfFunctionRaisesTheExactExceptionExpected(self):
        self.assert_matches("Right exception", raises(AssertionError), calling(raise_exception))

    def testDoesNotMatchTypeErrorIfActualIsNotCallable(self):
        self.assert_does_not_match("Not callable", raises(TypeError), 23)

    @pytest.mark.skipif(
        not (3, 0) <= sys.version_info < (3, 7), reason="Message differs between Python versions"
    )
    def testDoesNotMatchIfTheWrongExceptionTypeIsRaisedPy3(self):
        self.assert_does_not_match("Wrong exception", raises(IOError), calling(raise_exception))
        expected_message = (
            "AssertionError('(){}',) of type <class 'AssertionError'> was raised instead"
        )
        self.assert_mismatch_description(
            expected_message, raises(TypeError), calling(raise_exception)
        )

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="Message differs between Python versions")
    def testDoesNotMatchIfTheWrongExceptionTypeIsRaisedPy37(self):
        self.assert_does_not_match("Wrong exception", raises(IOError), calling(raise_exception))
        expected_message = (
            "AssertionError('(){}') of type <class 'AssertionError'> was raised instead"
        )
        self.assert_mismatch_description(
            expected_message, raises(TypeError), calling(raise_exception)
        )

    def testMatchesIfFunctionRaisesASubclassOfTheExpectedException(self):
        self.assert_matches("Subclassed Exception", raises(Exception), calling(raise_exception))

    def testMatchesIfFunctionRaisesASubclassOfTheExpectedBaseException(self):
        self.assert_matches(
            "Subclassed BasedException", raises(BaseException), calling(raise_baseException)
        )

    def testDoesNotMatchIfFunctionDoesNotRaiseException(self):
        self.assert_does_not_match("No exception", raises(ValueError), calling(no_exception))

    def testDoesNotMatchExceptionIfRegularExpressionDoesNotMatch(self):
        self.assert_does_not_match(
            "Bad regex", raises(AssertionError, "Phrase not found"), calling(raise_exception)
        )
        self.assert_mismatch_description(
            '''Correct assertion type raised, but the expected pattern ("Phrase not found") not found. Exception message was: "(){}"''',
            raises(AssertionError, "Phrase not found"),
            calling(raise_exception),
        )

    def testMatchesRegularExpressionToStringifiedException(self):
        self.assert_matches(
            "Regex",
            raises(AssertionError, "(3, 1, 4)"),
            calling(raise_exception).with_args(3, 1, 4),
        )

        self.assert_matches(
            "Regex",
            raises(AssertionError, r"([\d, ]+)"),
            calling(raise_exception).with_args(3, 1, 4),
        )

    def testMachesIfRaisedExceptionMatchesAdditionalMatchers(self):
        self.assert_matches(
            "Properties",
            raises(AssertionError, matching=has_properties(prip="prop")),
            calling(raise_exception_with_properties).with_args(prip="prop"),
        )

    def testDoesNotMatchIfAdditionalMatchersDoesNotMatch(self):
        self.assert_does_not_match(
            "Bad properties",
            raises(AssertionError, matching=has_properties(prop="prip")),
            calling(raise_exception_with_properties).with_args(prip="prop"),
        )
        self.assert_mismatch_description(
            '''Correct assertion type raised, but an object with a property 'prop' matching 'prip' not found. Exception message was: "boom"''',
            raises(AssertionError, matching=has_properties(prop="prip")),
            calling(raise_exception_with_properties).with_args(prip="prop"),
        )

    def testDoesNotMatchIfNeitherPatternOrMatcherMatch(self):
        self.assert_does_not_match(
            "Bad pattern and properties",
            raises(AssertionError, pattern="asdf", matching=has_properties(prop="prip")),
            calling(raise_exception_with_properties).with_args(prip="prop"),
        )
        self.assert_mismatch_description(
            '''Correct assertion type raised, but the expected pattern ("asdf") and an object with a property 'prop' matching 'prip' not found. Exception message was: "boom"''',
            raises(AssertionError, pattern="asdf", matching=has_properties(prop="prip")),
            calling(raise_exception_with_properties).with_args(prip="prop"),
        )

    def testDescribeMismatchWillCallItemIfNotTheOriginalMatch(self):
        function = Callable()
        matcher = raises(AssertionError)
        matcher.describe_mismatch(function, object())
        self.assertTrue(function.called)


@pytest.mark.parametrize(
    "expected_message",
    [
        pytest.param(
            "but AssertionError('(){}',) of type <type 'exceptions.AssertionError'> was raised.",
            marks=pytest.mark.skipif(
                sys.version_info >= (3, 0), reason="Message differs between Python versions"
            ),
        ),
        pytest.param(
            "but AssertionError('(){}',) of type <class 'AssertionError'> was raised.",
            marks=pytest.mark.skipif(
                not (3, 0) <= sys.version_info < (3, 7),
                reason="Message differs between Python versions",
            ),
        ),
        pytest.param(
            "but AssertionError('(){}') of type <class 'AssertionError'> was raised.",
            marks=pytest.mark.skipif(
                sys.version_info < (3, 7), reason="Message differs between Python versions"
            ),
        ),
    ],
)
def test_gives_correct_message_when_wrapped_with_is_not(expected_message):
    assert_mismatch_description(
        expected_message, not_(raises(AssertionError)), calling(raise_exception)
    )


class CallingTest(unittest.TestCase):
    def testCallingDoesNotImmediatelyExecuteFunction(self):
        try:
            calling(raise_exception)
        except AssertionError:
            self.fail()
        else:
            pass

    def testCallingObjectCallsProvidedFunction(self):
        method = Callable()
        calling(method)()
        self.assertTrue(method.called)

    def testCallingWithFunctionReturnsObject(self):
        method = Callable()
        callable = calling(method)
        returned = callable.with_args(3, 1, 4, keyword1="arg1")

        self.assertEqual(returned, callable)

    def testCallingWithFunctionSetsArgumentList(self):
        method = Callable()
        calling(method).with_args(3, 1, 4, keyword1="arg1")()

        self.assertEqual(method.args, (3, 1, 4))
        self.assertEqual(method.kwargs, {"keyword1": "arg1"})


class Callable(object):
    def __init__(self):
        self.called = False

    def __call__(self, *args, **kwargs):
        self.called = True
        self.args = args
        self.kwargs = kwargs
