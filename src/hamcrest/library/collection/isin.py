from typing import Iterable, TypeVar

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

T = TypeVar("T")


class IsIn(BaseMatcher[T]):
    def __init__(self, sequence: Iterable[T]) -> None:
        self.sequence = tuple(sequence)

    def _matches(self, item: T) -> bool:
        return item in self.sequence

    def describe_to(self, description: Description) -> None:
        description.append_text("one of ").append_list("(", ", ", ")", self.sequence)


def is_in(sequence: Iterable[T]) -> Matcher[T]:
    """Matches if evaluated object is present in a given sequence.

    :param sequence: The sequence to search.

    This matcher invokes the ``in`` membership operator to determine if the
    evaluated object is a member of the sequence.

    """
    return IsIn(sequence)
