from hamcrest.core.base_matcher import BaseMatcher, Matcher
from isequal import equal_to


class IsNot(BaseMatcher):
    """Calculates the logical negation of a matcher."""
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, item):
        return not self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('not ').append_description_of(self.matcher)


def is_not(item):
    if isinstance(item, Matcher):
        wrapped_item = item
    else:
        wrapped_item = equal_to(item)
    return IsNot(wrapped_item)
