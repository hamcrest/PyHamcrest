from hamcrest.core.base_matcher import BaseMatcher


class IsSame(BaseMatcher):
    """Is the value the same object as another value?"""
    
    def __init__(self, object):
        self.object = object

    def matches(self, item):
        return id(item) == id(self.object)

    def describe_to(self, description):
        description.append_text('same(')        \
                    .append_value(self.object)  \
                    .append_text(')')


same_instance = IsSame
