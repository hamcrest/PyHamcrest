from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AnyOf(BaseMatcher):

    def __init__(self, *matchers):
        self.matchers = matchers

    def _matches(self, item):
        for matcher in self.matchers:
            if matcher.matches(item):
                return True
        return False

    def describe_to(self, description):
        description.append_list('(', ' or ', ')', self.matchers)

    def describe_mismatch(self, item, mismatch_description):
        for matcher in self.matchers:
            if not matcher.matches(item):
                matcher.describe_mismatch(item, mismatch_description)
                return


def any_of(*items):
    """Matches if any of the given matchers evaluate to ``True``.

    :param matcher1,...:  A comma-separated list of matchers.

    The matchers are evaluated from left to right using short-circuit
    evaluation, so evaluation stops as soon as a matcher returns ``True``.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """
    return AnyOf(*[wrap_matcher(item) for item in items])
