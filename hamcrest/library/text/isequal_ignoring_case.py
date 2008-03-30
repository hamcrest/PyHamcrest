from hamcrest.core.base_matcher import BaseMatcher


class IsEqualIgnoringCase(BaseMatcher):

    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError('IsEqualIgnoringCase requires string')
        self.originalString = string
        self.lowerString = string.lower()
    
    def matches(self, item):
        if not isinstance(item, str):
            return False
        return self.lowerString == item.lower()

    def describe_to(self, description):
        description.append_text('eqIgnoringCase(')      \
                    .append_value(self.originalString)  \
                    .append_text(')')


equal_to_ignoring_case = IsEqualIgnoringCase
