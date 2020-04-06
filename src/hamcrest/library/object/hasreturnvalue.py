from typing import Any, Iterable, Mapping, Optional, TypeVar, Union, overload

from hamcrest import described_as
from hamcrest.core import not_none
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.allof import AllOf
from hamcrest.core.description import Description
from hamcrest.core.helpers.wrap_matcher import wrap_matcher as wrap_shortcut
from hamcrest.core.matcher import Matcher
from hamcrest.core.string_description import StringDescription

__author__ = "Perry Goy"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

V = TypeVar("V")


class IsObjectWithCallableProducingValue(BaseMatcher[object]):
    def __init__(
        self,
        method_name: str,
        value_matcher: Matcher[V],
        args: Iterable[Any] = None,
        kwargs: Mapping[str, Any] = None,
    ) -> None:
        self.method_name = method_name
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.value_matcher = value_matcher

    def get_callargs_str(self):
        args_str = ", ".join(map(str, self.args)) if self.args else ""

        kwargs_str = ""
        if self.kwargs:
            kwargs_bits = map(
                lambda x: "=".join(map(str, x)), sorted(self.kwargs.items(), key=lambda x: x[0])
            )
            kwargs_str = ", ".join(kwargs_bits)

        if args_str and kwargs_str:
            kwargs_str = ", " + kwargs_str

        return "(" + args_str + kwargs_str + ")"

    def get_return_value(self, item):
        return getattr(item, self.method_name)(*self.args, **self.kwargs)

    def _matches(self, item: object) -> bool:
        if item is None:
            return False

        if not hasattr(item, self.method_name):
            return False

        return_value = self.get_return_value(item)
        return self.value_matcher.matches(return_value)

    def describe_to(self, description: Description) -> None:
        description.append_text("an object with a method '").append_text(
            self.method_name
        ).append_text("' whose return value when called with ").append_text(
            self.get_callargs_str()
        ).append_text(
            " matches "
        ).append_description_of(
            self.value_matcher
        )

    def describe_mismatch(self, item: object, mismatch_description: Description) -> None:
        if item is None:
            mismatch_description.append_text("was None")
            return

        if not hasattr(item, self.method_name):
            mismatch_description.append_description_of(item).append_text(
                " did not have a "
            ).append_description_of(self.method_name).append_text(" method")
            return

        mismatch_description.append_text("method ").append_description_of(
            self.method_name
        ).append_text(" called with ").append_text(self.get_callargs_str()).append_text(" ")

        self.value_matcher.describe_mismatch(self.get_return_value(item), mismatch_description)

    def __str__(self):
        d = StringDescription()
        self.describe_to(d)
        return str(d)


def has_return_value(
    name: str,
    match: Optional[Union[Matcher[V], V]] = None,
    args: Iterable[Any] = None,
    kwargs: Mapping[str, Any] = None,
) -> Matcher[object]:
    """Matches if object has a method with a given name whose return value when
    called with the given args and kwargs satisfies a given matcher.

    :param name: The name of the method.
    :param match: Optional matcher to satisfy.
    :param args: Optional list of arguments to pass to the method.
    :param kwargs: Optional mapping of keyword arguments to pass to the method.

    This matcher determines if the evaluated object has a method with a given
    name. If no such method is found, ``has_return_value`` is not satisfied.

    If the method is found, it is called with the given arguments and keyword
    arguments, and its return value is passed to a given matcher for 
    evaluation. If the ``match`` argument is not a matcher, it is implicitly
    wrapped in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to
    check for equality.

    If the ``match`` argument is not provided, the
    :py:func:`~hamcrest.core.core.isnone.not_none` matcher is used so that
    ``has_return_value`` is satisfied if a matching method is found which
    returns something.

    Examples::

        has_return_value('is_displayed', True)
        has_return_value('get_child', is_instance_of(Child))
        has_return_value('name')

    """

    if match is None:
        match = not_none()

    return IsObjectWithCallableProducingValue(name, wrap_shortcut(match), args=args, kwargs=kwargs)
