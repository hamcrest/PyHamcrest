from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class AnyOf(BaseMatcher):
    """Calculates the logical disjunction of multiple matchers.

    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns ``True``.

    """

    def __init__(self, *matchers):
        self.matchers = matchers

    def _matches(self, item):
        for matcher in self.matchers:
            if matcher.matches(item):
                return True
        return False

    def describe_to(self, description):
        description.append_list('(', ' or ', ')', self.matchers)


def any_of(*items):
    """Evaluates to ``True`` if *any* of the passed in matchers evaluate to
    ``True``.

    :param items: Each item is a matcher, or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    """
    return AnyOf(*[wrap_matcher(item) for item in items])
