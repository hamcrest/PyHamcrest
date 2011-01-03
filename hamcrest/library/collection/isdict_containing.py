__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher


class IsDictContaining(BaseMatcher):
    """Matches dictionaries containing a key-value pair satisfying a given pair
    of matchers.

    """

    def __init__(self, key_matcher, value_matcher):
        self.key_matcher = key_matcher
        self.value_matcher = value_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'iteritems'):
            for key, value in dictionary.iteritems():
                if self.key_matcher.matches(key) and self.value_matcher.matches(value):
                    return True
        return False

    def describe_to(self, description):
        description.append_text('dictionary containing [')          \
                    .append_description_of(self.key_matcher)        \
                    .append_text(': ')                              \
                    .append_description_of(self.value_matcher)      \
                    .append_text(']')


def has_entry(key, value):
    """Matches dictionaries containing a key-value pair satisfying a given pair
    of matchers.

    :param key: A matcher - or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching - for the key.
    :param value: A matcher - or a value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching - for the
        value.

    """
    return IsDictContaining(wrap_matcher(key), wrap_matcher(value))
