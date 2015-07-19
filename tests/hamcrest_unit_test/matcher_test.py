from hamcrest.core.string_description import StringDescription
import sys
import pytest

try:
    from unittest import skipIf
    import unittest
except ImportError:
    import unittest2 as unittest

import logging

log = logging.getLogger(__name__)

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"
__tracebackhide__ = True


class MatcherTest(unittest.TestCase):

    def assert_matches(self, message, matcher, arg):
        assert_matches(matcher, arg, message)

    def assert_does_not_match(self, message, matcher, arg):
        assert_does_not_match(matcher, arg, message)

    def assert_description(self, expected, matcher):
        assert_description(expected, matcher)

    def assert_no_mismatch_description(self, matcher, arg):
        assert_no_mismatch_description(matcher, arg)

    def assert_mismatch_description(self, expected, matcher, arg):
        assert_mismatch_description(expected, matcher, arg)

    def assert_describe_mismatch(self, expected, matcher, arg):
        assert_describe_mismatch(expected, matcher, arg)


def assert_matches(matcher, arg, message):
    try:
        assert matcher.matches(arg), message
    except AssertionError:
        description = StringDescription()
        matcher.describe_mismatch(arg, description)
        log.error(str(description))
        raise


def assert_does_not_match(matcher, arg, message):
    assert not matcher.matches(arg), message


def assert_description(expected, matcher):
    description = StringDescription()
    description.append_description_of(matcher)
    assert expected == str(description)


def assert_no_mismatch_description(matcher, arg):
    description = StringDescription()
    result = matcher.matches(arg, description)
    assert result, 'Precondition: Matcher should match item'
    assert '' == str(description), 'Expected no mismatch description'


def assert_mismatch_description(expected, matcher, arg):
    description = StringDescription()
    result = matcher.matches(arg, description)
    assert not result, 'Precondition: Matcher should not match item'
    assert expected == str(description)


def assert_describe_mismatch(expected, matcher, arg):
    description = StringDescription()
    matcher.describe_mismatch(arg, description)
    assert expected == str(description)


only_py3 = pytest.mark.skipif(sys.version_info < (3, ),
                              reason="Only relevant in Python 3")
only_py2 = pytest.mark.skipif(sys.version_info >= (3, ),
                              reason="Only relevant in Python 2")
