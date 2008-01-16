from hamcrest.core.base_matcher import BaseMatcher
from isnot import not_


class IsNone(BaseMatcher):
    """Matches if value is None."""
    
    def matches(self, item):
        return item is None

    def describe_to(self, description):
        description.append_text('None')


none = IsNone

def not_none():
    return not_(none())
