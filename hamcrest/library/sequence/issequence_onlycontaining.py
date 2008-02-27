from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.anyof import any_of
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsSequenceOnlyContaining(BaseMatcher):
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, sequence):
        if not hasmethod(sequence, '__len__') or not hasmethod(sequence, '__iter__'):
            return False
        
        if len(sequence) == 0:
			return False
        for item in sequence:
            if not self.matcher.matches(item):
                return False
        return True

    def describe_to(self, description):
        description.append_text('a sequence only containing ')      \
                    .append_description_of(self.matcher)


def only_contains(*items):
    matchers = []
    for item in items:
        matchers.append(wrap_shortcut(item))    
    return IsSequenceOnlyContaining(apply(any_of, matchers))
