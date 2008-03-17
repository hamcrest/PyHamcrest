from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringEndsWith(BaseMatcher):
    """Tests if the argument is a string that ends with a substring."""

    def __init__(self, substring):
        if not isinstance(substring, str):
            raise TypeError('StringEndsWith requires string')
        self.substring = substring
    
    def matches(self, item):
        if not hasmethod(item, 'endswith'):
            return False
        return item.endswith(self.substring)

    def describe_to(self, description):
        description.append_text('a string ending with ')    \
                    .append_value(self.substring)


ends_with = StringEndsWith
