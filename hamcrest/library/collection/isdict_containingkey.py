__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsDictContainingKey(BaseMatcher):

    def __init__(self, key_matcher):
        self.key_matcher = key_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'iterkeys'):
            for key in dictionary.iterkeys():
                if self.key_matcher.matches(key):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary with key ')          \
                    .append_description_of(self.key_matcher)


def has_key(key):
    return IsDictContainingKey(wrap_shortcut(key))
