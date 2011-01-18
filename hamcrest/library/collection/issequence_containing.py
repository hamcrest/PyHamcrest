__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.allof import all_of
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class IsSequenceContaining(BaseMatcher):
    """Matches a sequence if any element satisfies a given matcher."""

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

#------------------------------------------------------------------------------

def has_item(item):
    """Matches a sequence if any element satifies a given matcher.

    :param item: A matcher, or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    """
    return IsSequenceContaining(wrap_matcher(item))


def has_items(*items):
    """Matches a sequence if all matchers are satisfied by any of the
    sequence's elements.

    """

    matchers = []
    for item in items:
        matchers.append(has_item(item))
    return apply(all_of, matchers)
