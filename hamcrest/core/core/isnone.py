__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from isnot import is_not


class IsNone(BaseMatcher):
    """Matches if value is None."""

    def _matches(self, item):
        return item is None

    def describe_to(self, description):
        description.append_text('None')


def none():
    """Matches if value is None."""
    return IsNone()


def not_none():
    """Matches if value is not None."""
    return is_not(none())
