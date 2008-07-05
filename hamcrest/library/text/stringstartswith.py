from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringStartsWith(SubstringMatcher):
    """Matches if the item is a string that starts with a given substring."""
    
    def __init__(self, substring):
        super(StringStartsWith, self).__init__(substring)
    
    def matches(self, item):
        if not hasmethod(item, 'startswith'):
            return False
        return item.startswith(self.substring)

    def relationship(self):
        return 'starting with'


"""Is the value a string starting with a given substring?"""
starts_with = StringStartsWith  # Can use directly without a function.
