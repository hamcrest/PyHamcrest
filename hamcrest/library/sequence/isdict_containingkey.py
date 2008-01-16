from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsDictContainingKey(BaseMatcher):
    
    def __init__(self, key_matcher):
        self.key_matcher = key_matcher

    def matches(self, dictionary):
        if hasmethod(dictionary, 'iterkeys'):
            for key in dictionary.iterkeys():
                if self.key_matcher.matches(key):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary with key ')          \
                    .append_description_of(self.key_matcher)


def haskey(key):
    return IsDictContainingKey(wrap_shortcut(key))
