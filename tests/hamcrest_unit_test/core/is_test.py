from __future__ import absolute_import

from hamcrest.core.core.is_ import *

import six
import pytest

from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import *
from .nevermatch import NeverMatch

__author__ = "Chris Rose"
__copyright__ = "Copyright 2015 hamcrest.org"
__license__ = "BSD, see License.txt"

class OldClass:
    pass

@pytest.mark.parametrize('arg, identity', (
    (True, True),
    (False, False),
))
def test_delegates_matching_to_nested_matcher(arg, identity):
    assert_matches(is_(equal_to(identity)), arg, "should match")


@pytest.mark.parametrize('arg, identity', (
    (True, False),
    (False, True),
))
def test_delegates_mismatching_to_nested_matcher(arg, identity):
    assert_does_not_match(is_(equal_to(identity)), arg, "should match")


def test_description_should_pass_through_matcher():
    assert_description('<True>', is_(equal_to(True)))


equal_matches = pytest.mark.parametrize('arg, identity, desc', (
    ('A', 'A', "'A'"),
    (5 + 3, 8, "<8>"),
    pytest.mark.issue56((tuple(), (), "<()>")),
))

equal_mismatches = pytest.mark.parametrize('arg, identity, desc', (
    ('B', 'A', "'A'"),
    (5 + 4, 8, "<8>"),
))

@equal_matches
def test_provides_convenient_shortcut_for_is_equal_to(arg, identity, desc):
    assert_matches(is_(identity), arg, 'should match')


@equal_mismatches
def test_provides_convenient_shortcut_for_is_equal_to_false(arg, identity, desc):
    assert_does_not_match(is_(identity), arg, 'should not match')


@equal_matches
def test_description_uses_equal_to(arg, identity, desc):
    assert_description(desc, is_(identity))


@pytest.mark.parametrize('arg, identity', (
    ('A', str),
    (1, int),
    only_py2((OldClass(), OldClass)),
))
def test_provides_instanceof_shortcut(arg, identity):
    assert_matches(is_(identity), arg, "should match")


def test_successful_match_does_not_generate_mismatch_description():
    assert_no_mismatch_description(is_('A'), 'A')

def test_delegates_mismatch_description_to_nested_matcher():
    assert_mismatch_description(
                            NeverMatch.mismatch_description,
                            is_(NeverMatch()),
                            'hi')

def test_delegates_describe_mismatch_to_nested_matcher():
    assert_describe_mismatch(
                            NeverMatch.mismatch_description,
                            is_(NeverMatch()),
                            'hi')


if __name__ == '__main__':
    unittest.main()
