__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class HasString(BaseMatcher):
    """Matches if str(item) satisfies a nested matcher."""

    def __init__(self, str_matcher):
        self.str_matcher = str_matcher

    def _matches(self, item):
        return self.str_matcher.matches(str(item))

    def describe_to(self, description):
        description.append_text('str(')                         \
                    .append_description_of(self.str_matcher)    \
                    .append_text(')')


def has_string(x):
    """Evaluates whether str(item) satisfies a given matcher, providing a
    shortcut to the frequently used has_string(equal_to(x))

    For example:  has_string(equal_to(x))
             vs.  has_string(x)
    """
    return HasString(wrap_shortcut(x))
