__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.anyof import any_of
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class IsSequenceOnlyContaining(BaseMatcher):
    """Matches sequences that only contain elements satisfying a given
    matcher.

    This matcher will never match an empty sequence.

    """

    def __init__(self, matcher):
        self.matcher = matcher

    def _matches(self, sequence):
        if not hasmethod(sequence, '__len__')   \
        or not hasmethod(sequence, '__iter__'):
            return False

        if len(sequence) == 0:
            return False
        for item in sequence:
            if not self.matcher.matches(item):
                return False
        return True

    def describe_to(self, description):
        description.append_text('a sequence containing items matching ')    \
                    .append_description_of(self.matcher)

#------------------------------------------------------------------------------

def only_contains(*items):
    """Matches sequences that only contain elements satisfying any of a list
    of items.

    For example, ``[3,1,2]`` would satisfy ``only_contains(less_than(4))``.

    If an item is not a matcher, it is equivalent to ``equal_to(item)``, so the
    list in the example above would also satisfy ``only_contains(1,2,3)``.

    """
    matchers = []
    for item in items:
        matchers.append(wrap_matcher(item))
    return IsSequenceOnlyContaining(apply(any_of, matchers))
