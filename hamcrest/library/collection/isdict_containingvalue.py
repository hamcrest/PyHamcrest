__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class IsDictContainingValue(BaseMatcher):
    """Matches dictionaries containing a value satisfying a given matcher."""

    def __init__(self, value_matcher):
        self.value_matcher = value_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'itervalues'):
            for value in dictionary.itervalues():
                if self.value_matcher.matches(value):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary with value ')       \
                    .append_description_of(self.value_matcher)


def has_value(value):
    """Matches dictionaries containing a value satisfying a given matcher.

    :param value: A matcher - or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching - for the
        value.

    """
    return IsDictContainingValue(wrap_matcher(value))
