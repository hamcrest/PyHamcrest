from hamcrest.core.base_matcher import BaseMatcher


class IsInstanceOf(BaseMatcher):
    """Tests whether the value is an instance of a class."""
    
    def __init__(self, the_class):
        if not isinstance(the_class, type):
            raise TypeError('IsInstanceOf requires type')
        self.the_class = the_class

    def matches(self, item):
        return isinstance(item, self.the_class)

    def describe_to(self, description):
        description.append_text('an instance of ')          \
                    .append_text(self.the_class.__name__)


instance_of = IsInstanceOf
