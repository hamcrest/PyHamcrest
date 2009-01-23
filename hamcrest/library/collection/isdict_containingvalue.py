from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsDictContainingValue(BaseMatcher):
    
    def __init__(self, value_matcher):
        self.value_matcher = value_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'itervalues'):
            for value in dictionary.itervalues():
                if self.value_matcher.matches(value):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary with value ')       \
                    .append_description_of(self.value_matcher)


def has_value(value):
    return IsDictContainingValue(wrap_shortcut(value))
