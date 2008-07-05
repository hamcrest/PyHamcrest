from hamcrest.core.base_matcher import BaseMatcher


def _comparison(compare):
    if compare > 0:
        return 'less than'
    elif compare == 0:
        return 'equal to'
    else:
        return 'greater than'


class OrderingComparison(BaseMatcher):
    
    def __init__(self, value, min_compare, max_compare):
        self.value = value
        self.min_compare = min_compare
        self.max_compare = max_compare

    def matches(self, item):
        compare = cmp(self.value, item)
        return self.min_compare <= compare and compare <= self.max_compare

    def describe_to(self, description):
        description.append_text('a value ').append_text(_comparison(self.min_compare))
        if self.min_compare != self.max_compare:
            description.append_text(' or ').append_text(_comparison(self.max_compare))
        description.append_text(' ').append_value(self.value)



def greater_than(value):
    """Is value > expected?"""
    return OrderingComparison(value, -1, -1)

def greater_than_or_equal_to(value):
    """Is value >= expected?"""
    return OrderingComparison(value, -1, 0)

def less_than(value):
    """Is value < expected?"""
    return OrderingComparison(value, 1, 1)

def less_than_or_equal_to(value):
    """Is value <= expected?"""
    return OrderingComparison(value, 0, 1)
