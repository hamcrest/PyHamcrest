__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

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

#------------------------------------------------------------------------------

def anything(description=None):
    """This matcher always evaluates to ``True``.

    You can optionally supply a meaningful string used when describing itself.

    """
    return IsAnything(description)
