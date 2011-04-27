from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Romilly Cocking"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class StringContainsInOrder(BaseMatcher):
    def __init__(self, *substrings):
        self._substrings = substrings

    def matches(self, item, mismatch_description=None):
        from_index = 0
        for substring in self._substrings:
            from_index = item.find(substring, from_index)
            if from_index == -1:
                return False
        return True

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('was %s' % repr(item))

    def describe_to(self, description):
        description.append_value_list('a string containing ',', ',' in order', self._substrings )


def contains_in_order(*substrings):
    return StringContainsInOrder(*substrings)
