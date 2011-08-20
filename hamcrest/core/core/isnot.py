__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher, Matcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from isequal import equal_to


class IsNot(BaseMatcher):

    def __init__(self, matcher):
        self.matcher = matcher

    def _matches(self, item):
        return not self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('not ').append_description_of(self.matcher)


def is_not(match):
    """Inverts the given matcher to its logical negation.

    :param match: The matcher to negate.

    This matcher compares the evaluated object to the negation of the given
    matcher. If the ``match`` argument is not a matcher, it is implicitly
    wrapped in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to
    check for equality, and thus matches for inequality.

    Examples::

        assert_that(cheese, is_not(equal_to(smelly)))
        assert_that(cheese, is_not(smelly))

    """
    return IsNot(wrap_matcher(match))
