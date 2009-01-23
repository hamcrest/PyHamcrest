from hamcrest.core.base_matcher import BaseMatcher


class IsEqual(BaseMatcher):
    """Is the value equal to another value?"""
    
    def __init__(self, equals):
        self.object = equals

    def _matches(self, item):
        return item == self.object

    def describe_to(self, description):
        description.append_value(self.object)


"""Is the value equal to another value?"""
equal_to = IsEqual  # Can use directly without a function.
