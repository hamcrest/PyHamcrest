__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher


class IsEqualIgnoringCase(BaseMatcher):
    """Matches if strings are equal ignoring case."""

    def __init__(self, string):
        if not isinstance(string, basestring):
            raise TypeError('IsEqualIgnoringCase requires string')
        self.original_string = string
        self.lowered_string = string.lower()

    def _matches(self, item):
        if not isinstance(item, basestring):
            return False
        return self.lowered_string == item.lower()

    def describe_to(self, description):
        description.append_description_of(self.original_string)    \
                   .append_text(' ignoring case')


def equal_to_ignoring_case(string):
    """Are the strings equal, ignoring case?"""
    return IsEqualIgnoringCase(string)
