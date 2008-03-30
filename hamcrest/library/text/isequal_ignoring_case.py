from hamcrest.core.base_matcher import BaseMatcher


class IsEqualIgnoringCase(BaseMatcher):

    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError('IsEqualIgnoringCase requires string')
        self.original_string = string
        self.lowered_string = string.lower()
    
    def matches(self, item):
        if not isinstance(item, str):
            return False
        return self.lowered_string == item.lower()

    def describe_to(self, description):
        description.append_text('eqIgnoringCase(')      \
                    .append_value(self.original_string)  \
                    .append_text(')')


equal_to_ignoring_case = IsEqualIgnoringCase
