from hamcrest.core.base_matcher import BaseMatcher


class AllOf(BaseMatcher):
    """Calculates the logical conjunction of multiple matchers.
    
    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns False.
    """
    
    def __init__(self, *matchers):
        self.matchers = matchers
    
    def matches(self, item, mismatch_description=None):
        for matcher in self.matchers:
            if not matcher.matches(item):
                if mismatch_description:
                    mismatch_description.append_description_of(matcher)         \
                                        .append_text(' ')
                    matcher.describe_mismatch(item, mismatch_description)
                return False
        return True
    
    def describe_mismatch(self, item, mismatch_description):
        self.matches(item, mismatch_description)
    
    def describe_to(self, description):
        description.append_list('(', ' and ', ')', self.matchers)


"""Evaluates to true only if ALL of the passed in matchers evaluate to true."""
all_of = AllOf  # Can use directly without a function.
