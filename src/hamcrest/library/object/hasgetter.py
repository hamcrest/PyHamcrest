from typing import Any, Mapping, TypeVar, Union, overload

from hamcrest import described_as
from hamcrest.core import anything
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.allof import AllOf
from hamcrest.core.description import Description
from hamcrest.core.helpers.wrap_matcher import wrap_matcher as wrap_shortcut
from hamcrest.core.matcher import Matcher
from hamcrest.core.string_description import StringDescription

__author__ = "Chris Rose;Thomas Hess"
__copyright__ = "Copyright 2011-2024 hamcrest.org"
__license__ = "BSD, see License.txt"

V = TypeVar("V")


class IsObjectWithGetter(BaseMatcher[object]):
    def __init__(self, property_name: str, value_matcher: Matcher[V]) -> None:
        self.property_name = property_name
        self.value_matcher = value_matcher

    def _matches(self, item: object) -> bool:
        if item is None:
            return False

        if not hasattr(item, self.property_name):
            return False

        getter = getattr(item, self.property_name)
        if not callable(getter):
            return False

        value = getter()
        return self.value_matcher.matches(value)

    def describe_to(self, description: Description) -> None:
        description.append_text("an object with a getter '").append_text(
            self.property_name
        ).append_text("' returning ").append_description_of(self.value_matcher)

    def describe_mismatch(self, item: object, mismatch_description: Description) -> None:
        if item is None:
            mismatch_description.append_text("was None")
            return

        if not hasattr(item, self.property_name):
            mismatch_description.append_description_of(item).append_text(
                " did not have the "
            ).append_description_of(self.property_name).append_text(" getter")
            return

        getter = getattr(item, self.property_name)
        if not callable(getter):
            mismatch_description.append_description_of(item).append_text(
                " attribute "
            ).append_description_of(self.property_name).append_text(" is not callable")
            return

        mismatch_description.append_text("getter ").append_description_of(
            self.property_name
        ).append_text(" return value ")
        value = getter()
        self.value_matcher.describe_mismatch(value, mismatch_description)

    def __str__(self):
        d = StringDescription()
        self.describe_to(d)
        return str(d)


def has_getter(name: str, match: Union[None, Matcher[V], V] = None) -> Matcher[Any]:
    """Matches if object has a callable getter with a given name whose return value satisfies
    a given matcher.

    :param name: The name of the getter.
    :param match: Optional matcher to satisfy.

    This matcher determines if the evaluated object has a callable getter with a given
    name. If no such getter is found or the found attribute is not callable,
    ``has_getter`` is not satisfied.

    If the getter is found and is callable, its return value is passed to a given matcher for
    evaluation. If the ``match`` argument is not a matcher, it is implicitly
    wrapped in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to
    check for equality.

    If the ``match`` argument is not provided, the
    :py:func:`~hamcrest.core.core.isanything.anything` matcher is used so that
    ``has_getter`` is satisfied if a matching getter is found.

    Examples::

        has_getter('name', starts_with('J'))
        has_getter('name', 'Jon')
        has_getter('name')

    """

    if match is None:
        match = anything()

    return IsObjectWithGetter(name, wrap_shortcut(match))


# Keyword argument form
@overload
def has_getters(**keys_valuematchers: Union[Matcher[V], V]) -> Matcher[Any]:
    ...


# Name to matcher dict form
@overload
def has_getters(keys_valuematchers: Mapping[str, Union[Matcher[V], V]]) -> Matcher[Any]:
    ...


# Alternating name/matcher form
@overload
def has_getters(*keys_valuematchers: Any) -> Matcher[Any]:
    ...


def has_getters(*keys_valuematchers, **kv_args) -> Matcher[Any]:
    """Matches if an object has callable getters satisfying all of a dictionary
    of string getter names and corresponding value matchers.

    :param keys_valuematchers: A dictionary mapping keys to associated value matchers,
        or to expected values for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    Note that the keys must be actual keys, not matchers. Any value argument
    that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    Examples::

        has_getters({'foo':equal_to(1), 'bar':equal_to(2)})
        has_getters({'foo':1, 'bar':2})
        has_getters({'x':  1, 'y':  2, 'area': less_than(100), 'height': greater_than(5)})

    ``has_getters`` also accepts a list of keyword arguments:

    .. function:: has_getters(keyword1=value_matcher1[, keyword2=value_matcher2[, ...]])

    :param keyword1: A keyword to look up.
    :param valueMatcher1: The matcher to satisfy for the value, or an expected
        value for :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    Examples::

        has_getters(foo=equal_to(1), bar=equal_to(2))
        has_getters(foo=1, bar=2)

    Finally, ``has_getters`` also accepts a list of alternating keys and their
    value matchers:

    .. function:: has_getters(key1, value_matcher1[, ...])

    :param key1: A key (not a matcher) to look up.
    :param valueMatcher1: The matcher to satisfy for the value, or an expected
        value for :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    Examples::

        has_getters('foo', equal_to(1), 'bar', equal_to(2))
        has_getters('foo', 1, 'bar', 2)

    """
    if len(keys_valuematchers) == 1:
        try:
            base_dict = keys_valuematchers[0].copy()
            for key in base_dict:
                base_dict[key] = wrap_shortcut(base_dict[key])
        except AttributeError:
            raise ValueError(
                "single-argument calls to has_getters must pass a dict as the argument"
            )
    else:
        if len(keys_valuematchers) % 2:
            raise ValueError("has_getters requires key-value pairs")
        base_dict = {}
        for index in range(int(len(keys_valuematchers) / 2)):
            base_dict[keys_valuematchers[2 * index]] = wrap_shortcut(
                keys_valuematchers[2 * index + 1]
            )

    for key, value in kv_args.items():
        base_dict[key] = wrap_shortcut(value)

    if len(base_dict) > 1:
        description = StringDescription().append_text("an object with getters ")
        for i, (property_name, property_value_matcher) in enumerate(sorted(base_dict.items())):
            description.append_description_of(property_name).append_text(
                " returning "
            ).append_description_of(property_value_matcher)
            if i < len(base_dict) - 1:
                description.append_text(" and ")

        return described_as(
            str(description),
            AllOf(
                *[
                    has_getter(property_name, property_value_matcher)
                    for property_name, property_value_matcher in sorted(base_dict.items())
                ],
                describe_all_mismatches=True,
                describe_matcher_in_mismatch=False,
            ),
        )
    else:
        property_name, property_value_matcher = base_dict.popitem()
        return has_getter(property_name, property_value_matcher)
