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

    def __init__(self, value_matchers):
        self.value_matchers = value_matchers

    def _not_a_dictionary(self, dictionary, mismatch_description):
        if mismatch_description:
            mismatch_description.append_description_of(dictionary) \
                                .append_text(' is not a mapping object')
        return False

    def matches(self, dictionary, mismatch_description=None):
        for key in self.value_matchers:

            try:
                if not key in dictionary:
                    if mismatch_description:
                        mismatch_description.append_text('no ')             \
                                            .append_description_of(key)     \
                                            .append_text(' key in ')        \
                                            .append_description_of(dictionary)
                    return False
            except TypeError:
                return self._not_a_dictionary(dictionary, mismatch_description)

            value_matcher = self.value_matchers[key]
            try:
                actual_value = dictionary[key]
            except TypeError:
                return self._not_a_dictionary(dictionary, mismatch_description)

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
        description.append_description_of(index)                        \
                   .append_text(': ')                                   \
                   .append_description_of(self.value_matchers[index])

    def describe_to(self, description):
        description.append_text('a dictionary containing {')
        first = True
        for key in self.value_matchers:
            if not first:
                description.append_text(', ')
            self.describe_keyvalue(key, description)
            first = False
        description.append_text('}')


def has_entries(*keys_valuematchers, **kv_args):
    """Matches dictionaries containing key-value pairs satisfying a given list
    of alternating keys and value matchers.

    :param keys_valuematchers: Alternating pairs of keys and value matchers (or
        straight values for :py:func:`~hamcrest.core.core.isequal.equal_to`
        matching.

    """
    if len(keys_valuematchers) == 1:
        try:
            base_dict = keys_valuematchers[0].copy()
        except AttributeError:
            raise ValueError('single-argument calls to has_entries must pass a dict as the argument')
    else:
        if len(keys_valuematchers) % 2:
            raise ValueError('has_entries requires key-value pairs')
        base_dict = {}
        for index in range(int(len(keys_valuematchers) / 2)):
            base_dict[keys_valuematchers[2 * index]] = wrap_matcher(keys_valuematchers[2 * index + 1])

    for key, value in kv_args.items():
        base_dict[key] = wrap_matcher(value)

    return IsDictContainingEntries(base_dict)
