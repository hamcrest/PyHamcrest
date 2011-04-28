from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Romilly Cocking"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class StringContainsInOrder(BaseMatcher):
    def __init__(self, *substrings):
        self.substrings = substrings

    def _matches(self, item):
        from_index = 0
        for substring in self.substrings:
            from_index = item.find(substring, from_index)
            if from_index == -1:
                return False
        return True

    def describe_to(self, description):
        description.append_list('a string containing ', ', ', ' in order', self.substrings)


def string_contains_in_order(*substrings):
    return StringContainsInOrder(*substrings)
