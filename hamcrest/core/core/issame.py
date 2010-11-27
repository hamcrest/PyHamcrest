__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


class IsSame(BaseMatcher):
    """Is the value the same object as another value?"""

    def __init__(self, object):
        self.object = object

    def _matches(self, item):
        return item is self.object

    def describe_to(self, description):
        description.append_text('same_instance(')   \
                    .append_value(self.object)      \
                    .append_text(')')

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('was ')        \
                            .append_value(item)         \
                            .append_text(' with id ')
        mismatch_description.append(str(id(item)))


def same_instance(object):
    """Evaluates to True only when the argument is this same object."""
    return IsSame(object)
