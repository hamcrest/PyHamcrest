from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Chris Rose"
__copyright__ = "Copyright 2012 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsEmpty(BaseMatcher):

    def matches(self, item, mismatch_description=None):
        try:
            if len(item) == 0:
                return True

            if mismatch_description:
                mismatch_description \
                    .append_text('has %d item(s)' % len(item))

        except TypeError:
            if mismatch_description:
                mismatch_description \
                    .append_text('does not support length')

            return False

    def describe_to(self, description):
        description.append_text('an empty collection')


class HasLength(BaseMatcher):

    def __init__(self, length):
        self.length = length

    def matches(self, item, mismatch_description=None):
        try:
            if len(item) == self.length:
                return True

            if mismatch_description:
                mismatch_description \
                    .append_text('has %d item(s)' % len(item))

        except TypeError:
            if mismatch_description:
                mismatch_description \
                    .append_text('does not support length')

            return False

    def describe_to(self, description):
        description.append_text('a collection with %d item(s)' % self.length)


def empty():
    """
    This matcher matches any collection-like object that responds to the
    __len__ method, and has a length of 0.
    """
    return Empty()

def has_length(len_):
    """
    This matcher matches any collection-like object that responds to the
    __len__ method, and has the specified length.
    """
    return HasLength(len_)
