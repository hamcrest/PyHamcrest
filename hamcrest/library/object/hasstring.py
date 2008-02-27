from hamcrest.core.base_matcher import BaseMatcher


class HasString(BaseMatcher):
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, item):
        return self.matcher.matches(str(item))

    def describe_to(self, description):
        description.append_text('str(')                     \
                    .append_description_of(self.matcher)    \
                    .append_text(')')


has_string = HasString
