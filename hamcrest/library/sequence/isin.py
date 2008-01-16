from hamcrest.core.base_matcher import BaseMatcher


class IsIn(BaseMatcher):
    
    def __init__(self, sequence):
        self.sequence = sequence

    def matches(self, item):
        return item in self.sequence

    def describe_to(self, description):
        description.append_text('one of ')      \
                    .append_value_list('(', ', ', ')', self.sequence)


isin = IsIn
