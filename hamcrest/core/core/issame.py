__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher


class IsSame(BaseMatcher):
    """Is the value the same object as another value?"""

    def __init__(self, object):
        self.object = object

    def _matches(self, item):
        return item is self.object

    def describe_to(self, description):
        description.append_text('same instance as ')            \
                   .append_text(hex(id(self.object)))           \
                   .append_text(' ')                            \
                   .append_description_of(self.object)          \

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('was ')                \
                            .append_text(hex(id(item)))         \
                            .append_text(' ')                   \
                            .append_description_of(item)

#------------------------------------------------------------------------------

def same_instance(object):
    """Evaluates to ``True`` only when the argument is this same object."""
    return IsSame(object)
