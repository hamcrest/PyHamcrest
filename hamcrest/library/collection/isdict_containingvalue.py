__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_shortcut import wrap_shortcut


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
