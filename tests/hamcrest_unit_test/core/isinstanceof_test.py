import sys
import pytest

if __name__ == '__main__':
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.core.core.isinstanceof import *

from hamcrest_unit_test.matcher_test import *

__author__ = "Chris Rose"
__copyright__ = "Copyright 2015 hamcrest.org"
__license__ = "BSD, see License.txt"

class Parent:
    pass

class Child(Parent):
    pass


@pytest.mark.parametrize('arg, matcher', (
    (1, instance_of(int)),
    (1, instance_of((str, int))),
    ('foo', instance_of((str, int))),
    (1, instance_of((int, str))),
    ('foo', instance_of((int, str))),
    only_py2((Parent(), instance_of(Parent))),
))
def test_matching_evaluation(arg, matcher):
    assert_matches(matcher, arg, 'same class')


@pytest.mark.parametrize('arg, matcher', (
    ('hi', instance_of(int)),
    (None, instance_of(int)),
    only_py2(('not a parent', instance_of(Parent))),
    only_py2((None, instance_of(Parent))),
))
def test_mismatching_evaluation(arg, matcher):
    assert_does_not_match(matcher, arg, 'mismatched')

@pytest.mark.parametrize('obj', (
    pytest.mark.issue56(()),
    'str',
))
def test_matcher_creation_requires_type(obj):
    with pytest.raises(TypeError):
        instance_of(obj)

@pytest.mark.parametrize('desc, type', (
    ('an instance of int', int),
    ('an instance of Parent', Parent)
))
def test_has_a_readable_description(desc, type):
    assert_description(desc, instance_of(type));

def test_successful_match_does_not_generate_mismatch_description():
    assert_no_mismatch_description(instance_of(int), 3)

def test_mismatch_description_shows_actual_argument():
    assert_mismatch_description("was 'bad'", instance_of(int), 'bad')

def test_describe_mismatch():
    assert_describe_mismatch("was 'bad'", instance_of(int), 'bad')
