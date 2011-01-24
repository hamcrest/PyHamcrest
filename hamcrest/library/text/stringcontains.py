__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class StringContains(SubstringMatcher):
    """Matches if the item is a string that contains a given substring."""

    def __init__(self, substring):
        super(StringContains, self).__init__(substring)

    def _matches(self, item):
        if not hasmethod(item, 'find'):
            return False
        return item.find(self.substring) >= 0

    def relationship(self):
        return 'containing'

#------------------------------------------------------------------------------

def contains_string(substring):
    """Is the value a string containing a given substring?"""
    return StringContains(substring)
