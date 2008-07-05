from hamcrest.core.base_matcher import BaseMatcher
from isnot import is_not


class IsNone(BaseMatcher):
    """Matches if value is None."""
    
    def matches(self, item):
        return item is None

    def describe_to(self, description):
        description.append_text('None')


"""Matches if value is None."""
none = IsNone   # Can use directly without a function.

def not_none():
    """Matches if value is not None."""
    return is_not(none())
