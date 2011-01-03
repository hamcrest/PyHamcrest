__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class MatchInAnyOrder(object):
    def __init__(self, matchers, mismatch_description):
        self.matchers = matchers
        self.mismatch_description = mismatch_description

    def matches(self, item):
        return self.isnotsurplus(item) and self.ismatched(item)

    def isfinished(self, sequence):
        if not self.matchers:
            return True
        if self.mismatch_description:
            self.mismatch_description.append_text('No item matches: ')      \
                                .append_list('', ', ', '', self.matchers)   \
                                .append_text(' in ')                        \
                                .append_list('[', ', ', ']', sequence)
        return False

    def isnotsurplus(self, item):
        if not self.matchers:
            if self.mismatch_description:
                self.mismatch_description.append_text('Not matched: ')  \
                                         .append_description_of(item)
            return False
        return True

    def ismatched(self, item):
        index = 0
        for matcher in self.matchers:
            if matcher.matches(item):
                del self.matchers[index]
                return True
            index += 1
        if self.mismatch_description:
            self.mismatch_description.append_text('Not matched: ')  \
                                     .append_description_of(item)
        return False


class IsSequenceContainingInAnyOrder(BaseMatcher):
    """Matches a sequence if its elements, in any order, satisfy a list of
    matchers.

    """

    def __init__(self, matchers):
        self.matchers = matchers

    def matches(self, sequence, mismatch_description=None):
        if not hasmethod(sequence, '__iter__'):
            return False
        matchsequence = MatchInAnyOrder(self.matchers, mismatch_description)
        for item in sequence:
            if not matchsequence.matches(item):
                return False
        return matchsequence.isfinished(sequence)

    def describe_mismatch(self, item, mismatch_description):
        self.matches(item, mismatch_description)

    def describe_to(self, description):
        description.append_text('sequence over ') \
                   .append_list('[', ', ', ']', self.matchers) \
                   .append_text(' in any order')


def contains_inanyorder(*items):
    """Matches a sequence if its elements, in any order, satisfy a list of
    matchers.

    :param items: Each item is a matcher, or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    """

    matchers = []
    for item in items:
        matchers.append(wrap_matcher(item))
    return IsSequenceContainingInAnyOrder(matchers)
