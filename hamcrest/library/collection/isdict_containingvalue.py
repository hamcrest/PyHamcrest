from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingValue(BaseMatcher):
    """Matches dictionaries containing a value satisfying a given matcher."""

    def __init__(self, value_matcher):
        self.value_matcher = value_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'values'):
            for value in dictionary.values():
                if self.value_matcher.matches(value):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('a dictionary containing value ')   \
                    .append_description_of(self.value_matcher)


def has_value(value):
    """Matches dictionaries containing a value satisfying a given matcher.

    :param value: A matcher - or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching - for the
        value.

    """
    return IsDictContainingValue(wrap_matcher(value))
