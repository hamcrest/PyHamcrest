from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringStartsWith(BaseMatcher):

    def __init__(self, substring):
        if not isinstance(substring, str):
            raise TypeError('StringStartsWith requires string')
        self.substring = substring
    
    def matches(self, item):
        if not hasmethod(item, 'startswith'):
            return False
        return item.startswith(self.substring)

    def describe_to(self, description):
        description.append_text('a string starting with ')      \
                    .append_value(self.substring)


starts_with = StringStartsWith
