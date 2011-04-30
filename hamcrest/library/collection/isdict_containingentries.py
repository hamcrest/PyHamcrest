from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingEntries(BaseMatcher):
    """Matches dictionaries containing key-value pairs satisfying given lists
    of keys and value matchers.

    """

    def __init__(self, keys, value_matchers):
        self.keys = keys
        self.value_matchers = value_matchers

    def matches(self, dictionary, mismatch_description=None):
        if not isinstance(dictionary, dict):
            if mismatch_description:
                super(IsDictContainingEntries, self).   \
                    describe_mismatch(dictionary, mismatch_description)
            return False

        for index in range(len(self.keys)):
            key = self.keys[index]

            if not key in dictionary:
                if mismatch_description:
                    mismatch_description.append_text('no ')             \
                                        .append_description_of(key)     \
                                        .append_text(' key in ')        \
                                        .append_description_of(dictionary)
                return False

            value_matcher = self.value_matchers[index]
            actual_value = dictionary[key]

            if not value_matcher.matches(actual_value):
                if mismatch_description:
                    mismatch_description.append_text('value for ')  \
                                        .append_description_of(key) \
                                        .append_text(' ')
                    value_matcher.describe_mismatch(actual_value, mismatch_description)
                return False

        return True

    def describe_mismatch(self, item, mismatch_description):
        self.matches(item, mismatch_description)

    def describe_keyvalue(self, index, description):
        """Describes key-value pair at given index."""
        description.append_description_of(self.keys[index])             \
                   .append_text(': ')                                   \
                   .append_description_of(self.value_matchers[index])

    def describe_to(self, description):
        description.append_text('a dictionary containing {')
        for index in range(len(self.keys) - 1):
            self.describe_keyvalue(index, description)
            description.append_text(', ')
        index = len(self.keys) - 1
        self.describe_keyvalue(index, description)
        description.append_text('}')


def has_entries(*keys_valuematchers):
    """Matches dictionaries containing key-value pairs satisfying a given list
    of alternating keys and value matchers.

    :param keys_valuematchers: Alternating pairs of keys and value matchers (or
        straight values for :py:func:`~hamcrest.core.core.isequal.equal_to`
        matching.

    """
    if len(keys_valuematchers) % 2:
        raise SyntaxError('has_entries requires key-value pairs')
    keys = []
    value_matchers = []
    for index in range(int(len(keys_valuematchers) / 2)):
        keys.append(keys_valuematchers[2 * index])
        value_matchers.append(wrap_matcher(keys_valuematchers[2 * index + 1]))
    return IsDictContainingEntries(keys, value_matchers)
