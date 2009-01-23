from hamcrest.core.base_matcher import BaseMatcher


class AnyOf(BaseMatcher):
    """Calculates the logical disjunction of multiple matchers.
    
    Evaluation is shortcut, so subsequent matchers are not called if an earlier
    matcher returns True.
    """
    
    def __init__(self, *matchers):
        self.matchers = matchers
            
    def _matches(self, item):
        for matcher in self.matchers:
            if matcher.matches(item):
                return True
        return False
    
    def describe_to(self, description):
        description.append_list('(', ' or ', ')', self.matchers)


"""Evaluates to true if ANY of the passed in matchers evaluate to true."""
any_of = AnyOf  # Can use directly without a function.
