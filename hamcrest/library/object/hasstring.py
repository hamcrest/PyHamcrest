from hamcrest.core.base_matcher import BaseMatcher


class HasString(BaseMatcher):
    
    def __init__(self, str_matcher):
        self.str_matcher = str_matcher

    def matches(self, item):
        return self.str_matcher.matches(str(item))

    def describe_to(self, description):
        description.append_text('str(')                         \
                    .append_description_of(self.str_matcher)    \
                    .append_text(')')


has_string = HasString
