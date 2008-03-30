from hamcrest.core.base_matcher import BaseMatcher


class SubstringMatcher(BaseMatcher):
    
    def __init__(self, substring):
        if not isinstance(substring, str):
            raise TypeError(self.__class__.__name__ + ' requires string')
        self.substring = substring
    
    def describe_to(self, description):
        description.append_text('a string ')            \
                    .append_text(self.relationship())   \
                    .append_text(' ')                   \
                    .append_value(self.substring)
