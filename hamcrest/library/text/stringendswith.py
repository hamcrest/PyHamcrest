from hamcrest.library.text.substringmatcher import SubstringMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringEndsWith(SubstringMatcher):
    """Tests if the argument is a string that ends with a substring."""

    def __init__(self, substring):
        super(StringEndsWith, self).__init__(substring)
    
    def matches(self, item):
        if not hasmethod(item, 'endswith'):
            return False
        return item.endswith(self.substring)

    def relationship(self):
        return 'ending with'


ends_with = StringEndsWith
