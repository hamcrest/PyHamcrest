from hamcrest.core.base_matcher import BaseMatcher


def isnumeric(value):
    return isinstance(value, (int, long, float))


class IsCloseTo(BaseMatcher):
    """Is the value a number equal to a value within some range of acceptable
    error?
    """
    
    def __init__(self, value, error):
        if not isnumeric(value):
            raise TypeError('IsCloseTo value must be number')
        if not isnumeric(error):
            raise TypeError('IsCloseTo error must be number')
        
        self.value = value
        self.error = error

    def _matches(self, item):
        if not isnumeric(item):
            return False
        return abs(item - self.value) <= self.error

    def describe_to(self, description):
        description.append_text('a numeric value within ')  \
                    .append_value(self.error)               \
                    .append_text(' of ')                    \
                    .append_value(self.value)


"""Is the value a number equal to a value within some range of acceptable
error?
"""
close_to = IsCloseTo    # Can use directly without a function.
