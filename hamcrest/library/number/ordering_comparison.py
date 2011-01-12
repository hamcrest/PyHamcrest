__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
import operator


class OrderingComparison(BaseMatcher):

    def __init__(self, value, compare_func, comparison):
        self.value = value
        self.compare_func = compare_func
        self.comparison = comparison

    def _matches(self, item):
        return self.compare_func(item, self.value)

    def describe_to(self, description):
        description.append_text('a value ').append_text(self.comparison)
        description.append_text(' ').append_description_of(self.value)



def greater_than(value):
    """Is value > expected?"""
    return OrderingComparison(value, operator.gt, 'greater than')

def greater_than_or_equal_to(value):
    """Is value >= expected?"""
    return OrderingComparison(value, operator.ge, 'greater than or equal to')

def less_than(value):
    """Is value < expected?"""
    return OrderingComparison(value, operator.lt, 'less than')

def less_than_or_equal_to(value):
    """Is value <= expected?"""
    return OrderingComparison(value, operator.le, 'equal to or less than')
