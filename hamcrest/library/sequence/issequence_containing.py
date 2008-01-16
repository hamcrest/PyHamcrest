from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.allof import allof
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsSequenceContaining(BaseMatcher):
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, sequence):
        if hasmethod(sequence, '__iter__'):
            for item in sequence:
                if self.matcher.matches(item):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('a sequence containing ')           \
                    .append_description_of(self.matcher)


def hasitem(item):
    return IsSequenceContaining(wrap_shortcut(item))


def hasitems(*items):
    all = []
    for item in items:
        all.append(hasitem(item))
    return apply(allof, all)
