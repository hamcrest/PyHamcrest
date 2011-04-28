from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

__author__ = "Romilly Cocking"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class StringContainsInOrder(BaseMatcher):
    """Matches if the item is a string containing a given list of substrings,
    in order.

    """

    def __init__(self, *substrings):
        for substring in substrings:
            if not isinstance(substring, basestring):
                raise TypeError(self.__class__.__name__ + ' requires string arguments')
        self.substrings = substrings

    def _matches(self, item):
        if not hasmethod(item, 'find'):
            return False
        from_index = 0
        for substring in self.substrings:
            from_index = item.find(substring, from_index)
            if from_index == -1:
                return False
        return True

    def describe_to(self, description):
        description.append_list('a string containing ', ', ', ' in order', self.substrings)


def string_contains_in_order(*substrings):
    """Is the value a string containing a given list of substrings, in order?"""
    return StringContainsInOrder(*substrings)
