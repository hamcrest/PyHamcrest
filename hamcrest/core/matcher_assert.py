"""Unit test integration"""

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from matcher import Matcher
from string_description import StringDescription


def assert_that(arg1, arg2, arg3=''):
    """Asserts a match, or a boolean condition.

    If the assertion fails, ``assert_that`` raises an :py:exc:`AssertionError`.
    In the context of :py:class:`unittest.TestCase`, this will be reported as a
    test failure.

    When specified with a :py:class:`~hamcrest.core.matcher.Matcher` as the
    second argument, ``assert_that`` verifies a match::

        assert_that(actual, matcher)

    or ::

        assert_that(actual, matcher, reason)

    ``assert_that`` can also verify a boolean condition::

        assert_that(assertion, reason)

    This is equivalent to the :py:meth:`~unittest.TestCase.assert_` method of
    :py:class:`unittest.TestCase`, but because it's a standalone function, it
    offers greater flexibility in test writing.

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
                   .append_text('\n     but: ')
        matcher.describe_mismatch(actual, description)
        description.append_text('\n')
        raise AssertionError(str(description))


def _assert_bool(assertion, reason):
    if not assertion:
        raise AssertionError(reason)
