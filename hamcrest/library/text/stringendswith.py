__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class StringEndsWith(SubstringMatcher):
    """Matches if the item is a string that ends with a given substring."""

    def __init__(self, substring):
        super(StringEndsWith, self).__init__(substring)

    def _matches(self, item):
        if not hasmethod(item, 'endswith'):
            return False
        return item.endswith(self.substring)

    def relationship(self):
        return 'ending with'

#------------------------------------------------------------------------------

def ends_with(substring):
    """Is the value a string ending with a given substring?"""
    return StringEndsWith(substring)
