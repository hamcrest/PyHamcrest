__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


class IsAnything(BaseMatcher):
    """A matcher that always returns ``True``."""

    def __init__(self, description):
        self.description = description
        if not description:
            self.description = 'ANYTHING'

    def _matches(self, item):
        return True

    def describe_to(self, description):
        description.append_text(self.description)


def anything(description=None):
    """This matcher always evaluates to ``True``.

    You can optionally supply a meaningful string used when describing itself.

    """
    return IsAnything(description)
