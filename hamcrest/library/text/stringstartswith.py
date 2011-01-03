__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class StringStartsWith(SubstringMatcher):
    """Matches if the item is a string that starts with a given substring."""

    def __init__(self, substring):
        super(StringStartsWith, self).__init__(substring)

    def _matches(self, item):
        if not hasmethod(item, 'startswith'):
            return False
        return item.startswith(self.substring)

    def relationship(self):
        return 'starting with'


def starts_with(substring):
    """Is the value a string starting with a given substring?"""
    return StringStartsWith(substring)
