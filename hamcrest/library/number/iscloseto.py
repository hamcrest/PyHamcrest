__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


def isnumeric(value):
    return isinstance(value, (int, long, float))


class IsCloseTo(BaseMatcher):
    """Is the value a number equal to a value within some range of acceptable
    error?

    """

    def __init__(self, value, error):
        if not isnumeric(value):
            raise TypeError('IsCloseTo value must be number')
        if not isnumeric(error):
            raise TypeError('IsCloseTo error must be number')

        self.value = value
        self.error = error

    def _matches(self, item):
        if not isnumeric(item):
            return False
        return abs(item - self.value) <= self.error

    def describe_to(self, description):
        description.append_text('a numeric value within ')  \
                    .append_value(self.error)               \
                    .append_text(' of ')                    \
                    .append_value(self.value)


def close_to(value, error):
    """Is the value a number equal to a value within some range of acceptable
    error?

    """
    return IsCloseTo(value, error)
