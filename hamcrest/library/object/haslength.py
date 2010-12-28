__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class HasLength(BaseMatcher):
    """Does ``len(item)`` satisfy a given matcher?"""

    def __init__(self, len_matcher):
        self.len_matcher = len_matcher

    def _matches(self, item):
        if not hasmethod(item, '__len__'):
            return False
        return self.len_matcher.matches(len(item))

    def describe_to(self, description):
        description.append_text('len(')                         \
                    .append_description_of(self.len_matcher)    \
                    .append_text(')')


def has_length(x):
    """Evaluates whether ``len(item)`` satisfies a given matcher.

    :param x: A matcher, or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    Examples::

        has_length(greater_than(6))
        has_length(5)

    """
    return HasLength(wrap_matcher(x))
