__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from matcher import Matcher
from string_description import StringDescription


def assert_that(arg1, arg2, arg3=''):
    """Asserts a match, or a boolean condition.

    If the assertion fails, assert_match raises an AssertionError. In the
    context of unittest.TestCase, this will be reported as a test failure.

    When specified with a Matcher as the second argument, assert_that verifies
    a match:
        assert_that(actual, matcher)
    or
        assert_that(actual, matcher, reason)

    assert_that can also verify a boolean condition:
        assert_that(assertion, reason)
    This is equivalent to the unittest.TestCase.assert_ method, but because it
    is a standalone function, it offers greater flexibility in test writing.

    """
    if isinstance(arg2, Matcher):
        _assert_match(actual=arg1, matcher=arg2, reason=arg3)
    else:
        _assert_bool(assertion=arg1, reason=arg2)


def _assert_match(actual, matcher, reason):
    if not matcher.matches(actual):
        description = StringDescription()
        description.append_text(reason)             \
                   .append_text('\nExpected: ')     \
                   .append_description_of(matcher)  \
                   .append_text('\n     got: ')     \
                   .append_value(actual)            \
                   .append_text('\n')
        raise AssertionError(str(description))


def _assert_bool(assertion, reason):
    if not assertion:
        raise AssertionError(reason)
