from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringEndsWith(SubstringMatcher):
    """Matches if the item is a string that ends with a given substring."""

    def __init__(self, substring):
        super(StringEndsWith, self).__init__(substring)
    
    def matches(self, item):
        if not hasmethod(item, 'endswith'):
            return False
        return item.endswith(self.substring)

    def relationship(self):
        return 'ending with'


"""Is the value a string ending with a given substring?"""
ends_with = StringEndsWith  # Can use directly without a function.
