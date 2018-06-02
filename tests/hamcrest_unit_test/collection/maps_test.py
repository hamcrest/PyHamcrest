import pytest

from hamcrest import assert_that, equal_to, is_, less_than
from hamcrest.core.string_description import StringDescription
from hamcrest.library.collection.items_correspond_to import maps


@pytest.mark.parametrize(
    "a, b, matcher", [
        [[1, 2, 3], [4, 5, 6], less_than],
        [[2, 2, 2], [2, 2, 2], equal_to],
    ])
def test_maps_matcher(a, b, matcher):
    assert_that(a, maps(matcher, b))


def test_mismatch_description():
    a, b = [2, 2, 2], [2, 3, 2]
    mismatch_description = StringDescription()

    maps_matcher = maps(equal_to, a)
    assert_that(maps_matcher.matches(b),  is_(False))
    maps_matcher.describe_mismatch(b, mismatch_description)

    assert_that(str(mismatch_description), equal_to("\n          [1] was <3>"))
