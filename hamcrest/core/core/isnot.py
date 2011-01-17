__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher, Matcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from isequal import equal_to


class IsNot(BaseMatcher):
    """Calculates the logical negation of a matcher."""

    def __init__(self, matcher):
        self.matcher = matcher

    def _matches(self, item):
        return not self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('not ').append_description_of(self.matcher)

#------------------------------------------------------------------------------

def is_not(x):
    """Inverts the rule, providing a shortcut to the frequently used
    ``is_not(equal_to(x))``.

    For example::

        assert_that(cheese, is_not(equal_to(smelly)))

    vs. ::

        assert_that(cheese, is_not(smelly))

    """
    return IsNot(wrap_matcher(x))
