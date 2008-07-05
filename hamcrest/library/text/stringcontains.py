from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringContains(SubstringMatcher):
    """Matches if the item is a string that contains a given substring."""

    def __init__(self, substring):
        super(StringContains, self).__init__(substring)
    
    def matches(self, item):
        if not hasmethod(item, 'find'):
            return False
        return item.find(self.substring) >= 0
    
    def relationship(self):
        return 'containing'


"""Is the value a string containing a given substring?"""
contains_string = StringContains    # Can use directly without a function.
