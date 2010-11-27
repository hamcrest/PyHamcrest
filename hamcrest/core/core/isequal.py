__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


class IsEqual(BaseMatcher):
    """Is the value equal to another value?"""

    def __init__(self, equals):
        self.object = equals

    def _matches(self, item):
        return item == self.object

    def describe_to(self, description):
        description.append_value(self.object)


def equal_to(operand):
    """Is the value equal to another value?"""
    return IsEqual(operand)
