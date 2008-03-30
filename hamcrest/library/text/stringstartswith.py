from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringStartsWith(SubstringMatcher):
    """Tests if the argument is a string that starts with a substring."""
    
    def __init__(self, substring):
        super(StringStartsWith, self).__init__(substring)
    
    def matches(self, item):
        if not hasmethod(item, 'startswith'):
            return False
        return item.startswith(self.substring)

    def relationship(self):
        return 'starting with'


starts_with = StringStartsWith
