from hamcrest.core.base_matcher import BaseMatcher
from math import fabs

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


def isnumeric(value):
    return isinstance(value, (int, long, float))


class IsCloseTo(BaseMatcher):
    """Is the argument a number close to a value, within some delta?"""

    def __init__(self, value, delta):
        if not isnumeric(value):
            raise TypeError('IsCloseTo value must be numeric')
        if not isnumeric(delta):
            raise TypeError('IsCloseTo delta must be numeric')

        self.value = value
        self.delta = delta

    def _matches(self, item):
        if not isnumeric(item):
            return False
        return fabs(item - self.value) <= self.delta

    def describe_mismatch(self, item, mismatch_description):
        if not isnumeric(item):
            super(IsCloseTo, self).describe_mismatch(item, mismatch_description)
        else:
            actual_delta = fabs(item - self.value)
            mismatch_description.append_description_of(item)            \
                                .append_text(' differed by ')           \
                                .append_description_of(actual_delta)

    def describe_to(self, description):
        description.append_text('a numeric value within ')  \
                   .append_description_of(self.delta)       \
                   .append_text(' of ')                     \
                   .append_description_of(self.value)


def close_to(value, delta):
    """Is the argument a number close to a value, within some delta?"""
    return IsCloseTo(value, delta)
