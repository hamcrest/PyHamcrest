__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class HasString(BaseMatcher):
    """Does str(item) satisfy a given matcher?"""

    def __init__(self, str_matcher):
        self.str_matcher = str_matcher

    def _matches(self, item):
        return self.str_matcher.matches(str(item))

    def describe_to(self, description):
        description.append_text('str(')                         \
                    .append_description_of(self.str_matcher)    \
                    .append_text(')')


def has_string(x):
    """Evaluates whether str(item) satisfies a given matcher.

    Arguments:
    x -- A matcher, or a value for equal_to matching.

    Examples:
        has_string(starts_with('foo'))
        has_string('bar')

    """
    return HasString(wrap_matcher(x))
