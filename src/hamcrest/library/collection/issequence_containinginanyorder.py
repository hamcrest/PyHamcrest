from typing import Collection, Generic, Optional, TypeVar, Union

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from hamcrest.core.matcher import Matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

T = TypeVar("T")


class MatchInAnyOrder(Generic[T]):
    def __init__(
        self, matchers: Collection[Matcher[T]], mismatch_description: Optional[Description]
    ) -> None:
        self.matchers = list(matchers)
        self.mismatch_description = mismatch_description

    def matches(self, item: T) -> bool:
        return self.isnotsurplus(item) and self.ismatched(item)

    def isfinished(self, item: Collection[T]) -> bool:
        if not self.matchers:
            return True
        if self.mismatch_description:
            self.mismatch_description.append_text("no item matches: ").append_list(
                "", ", ", "", self.matchers
            ).append_text(" in ").append_list("[", ", ", "]", item)
        return False

    def isnotsurplus(self, item: T) -> bool:
        if not self.matchers:
            if self.mismatch_description:
                self.mismatch_description.append_text("not matched: ").append_description_of(item)
            return False
        return True

    def ismatched(self, item: T) -> bool:
        for index, matcher in enumerate(self.matchers):
            if matcher.matches(item):
                del self.matchers[index]
                return True

        if self.mismatch_description:
            self.mismatch_description.append_text("not matched: ").append_description_of(item)
        return False


class IsCollectionContainingInAnyOrder(BaseMatcher[Collection[T]]):
    def __init__(self, matchers: Collection[Matcher[T]]) -> None:
        self.matchers = matchers

    def matches(
        self, item: Collection[T], mismatch_description: Optional[Description] = None
    ) -> bool:
        try:
            collection = list(item)
            matchcollection = MatchInAnyOrder(self.matchers, mismatch_description)
            for element in collection:
                if not matchcollection.matches(element):
                    return False
            return matchcollection.isfinished(collection)
        except TypeError:
            if mismatch_description:
                super(IsCollectionContainingInAnyOrder, self).describe_mismatch(
                    item, mismatch_description
                )
            return False

    def describe_mismatch(self, item: Collection[T], mismatch_description: Description) -> None:
        self.matches(item, mismatch_description)

    def describe_to(self, description: Description) -> None:
        description.append_text("a sequence over ").append_list(
            "[", ", ", "]", self.matchers
        ).append_text(" in any order")


def contains_inanyorder(*items: Union[Matcher[T], T]) -> Matcher[Collection[T]]:
    """Matches if collection's elements, in any order, satisfy a given list of
    matchers.

    :param match1,...: A comma-separated list of matchers.

    This matcher iterates the evaluated collection, seeing if each element
    satisfies any of the given matchers. The matchers are tried from left to
    right, and when a satisfied matcher is found, it is no longer a candidate
    for the remaining elements. If a one-to-one correspondence is established
    between elements and matchers, ``contains_inanyorder`` is satisfied.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """

    matchers = []
    for item in items:
        matchers.append(wrap_matcher(item))
    return IsCollectionContainingInAnyOrder(matchers)


IsSequenceContainingInAnyOrder = IsCollectionContainingInAnyOrder
