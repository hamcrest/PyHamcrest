__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.matcher import Matcher


class IsEqual(BaseMatcher):
    """Is the value equal to another value?"""

    def __init__(self, equals):
        self.object = equals

    def _matches(self, item):
        return item == self.object

    def describe_to(self, description):
        nested_matcher = isinstance(self.object, Matcher)
        if nested_matcher:
            description.append_text('<')
        description.append_description_of(self.object)
        if nested_matcher:
            description.append_text('>')


def equal_to(operand):
    """Is the value equal to another value?"""
    return IsEqual(operand)
