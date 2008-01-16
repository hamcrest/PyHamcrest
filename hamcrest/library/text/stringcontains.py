from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod


class StringContains(BaseMatcher):

    def __init__(self, substring):
        if not isinstance(substring, str):
            raise TypeError('StringContains requires string')
        self.substring = substring
    
    def matches(self, item):
        if not hasmethod(item, 'find'):
            return False
        return item.find(self.substring) >= 0

    def describe_to(self, description):
        description.append_text('a string containing ')     \
                    .append_value(self.substring)


containsstring = StringContains
