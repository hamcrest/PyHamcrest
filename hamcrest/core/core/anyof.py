__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


class AnyOf(BaseMatcher):
    """Calculates the logical disjunction of multiple matchers.

    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns True.

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


def any_of(*matchers):
    """Evaluates to true if ANY of the passed in matchers evaluate to True."""
    return AnyOf(*matchers)
