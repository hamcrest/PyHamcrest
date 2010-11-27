__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_shortcut import wrap_shortcut


class IsDictContaining(BaseMatcher):

    def __init__(self, key_matcher, value_matcher):
        self.key_matcher = key_matcher
        self.value_matcher = value_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'iteritems'):
            for key, value in dictionary.iteritems():
                if self.key_matcher.matches(key) and self.value_matcher.matches(value):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary containing [')          \
                    .append_description_of(self.key_matcher)        \
                    .append_text(': ')                              \
                    .append_description_of(self.value_matcher)      \
                    .append_text(']')


def has_entry(key, value):
    return IsDictContaining(wrap_shortcut(key), wrap_shortcut(value))
