__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.allof import all_of
from hamcrest.core.internal.hasmethod import hasmethod
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class IsSequenceContaining(BaseMatcher):

    def __init__(self, element_matcher):
        self.element_matcher = element_matcher

    def _matches(self, sequence):
        if hasmethod(sequence, '__iter__'):
            for item in sequence:
                if self.element_matcher.matches(item):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('a sequence containing ')           \
                    .append_description_of(self.element_matcher)


def has_item(item):
    return IsSequenceContaining(wrap_shortcut(item))


def has_items(*items):
    all = []
    for item in items:
        all.append(has_item(item))
    return apply(all_of, all)
