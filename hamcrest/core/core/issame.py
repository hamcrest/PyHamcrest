from hamcrest.core.base_matcher import BaseMatcher


class IsSame(BaseMatcher):
    """Is the value the same object as another value?"""
    
    def __init__(self, object):
        self.object = object

    def _matches(self, item):
        return item is self.object

    def describe_to(self, description):
        description.append_text('same_instance(')                               \
                    .append_value(self.object)                                  \
                    .append_text(')')
    
    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('was ')                                \
                            .append_value(item)                                 \
                            .append_text(' with id ')
        mismatch_description.append(str(id(item)))

"""Evaluates to true only when the argument is this same object."""
same_instance = IsSame  # Can use directly without a function.
