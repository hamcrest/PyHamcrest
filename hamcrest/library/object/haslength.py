from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class HasLength(BaseMatcher):
    """Matches if len(item) satisfies a nested matcher."""

    def __init__(self, len_matcher):
        self.len_matcher = len_matcher

    def matches(self, item):
        if not hasmethod(item, '__len__'):
            return False
        return self.len_matcher.matches(len(item))

    def describe_to(self, description):
        description.append_text('len(')                         \
                    .append_description_of(self.len_matcher)    \
                    .append_text(')')


def has_length(x):
    """Evaluates whether len(item) satisfies a given matcher, providing a
    shortcut to the frequently used has_length(equal_to(x))
    
    For example:  has_length(equal_to(x))
             vs.  has_length(x)
    """
    return HasLength(wrap_shortcut(x))
