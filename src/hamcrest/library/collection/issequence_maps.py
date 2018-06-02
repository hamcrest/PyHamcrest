from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.string_description import StringDescription


class SequenceMapsMatcher(BaseMatcher):
    def __init__(self, matcher_callable, expected_items):
        self.matcher = matcher_callable
        self.expected = expected_items
        self.description = StringDescription()


    def _matches(self, actual_items):
        result = True
        for i, (exp, act) in enumerate(zip(self.expected, actual_items)):
            matcher = self.matcher(exp)
            if not matcher.matches(act):
                self.description.append_text("\n          [{0}] ".format(i))
                matcher.describe_mismatch(act, self.description)
                result = False
        return result


    def describe_to(self, description):
        description.append("A collection of items, containing:")
        for i, item in enumerate(self.expected):
            description.append_text(
                "\n          [{0}] ".format(i)
            ).append_description_of(
                self.matcher(item)
            )


    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append(self.description)


def maps(matcher_callable, items):
    """
    Matches if each item of the expected collection matches each corresponding
    item in the actual collection using the provided matcher_callable and
    in the same order.

    That is, if you provide :py:func:`~hamcrest.core.core.isequal.equal_to`
    as the matcher callable, the 0th item of your actual collection must be equal
    to the 0th item of you expected collection, 1st == 1st, and so on.

    Please note, that unlike in most other cases, you shouldn't call the matcher
    function/callable yourself.

    `assert_that([1, 2, 3], maps(equal_to, [1, 2, 3])`

    :param matcher_callable: The matcher callable that must be applied to the items.
    :type matcher_callable: :py:class:`~hamcrest.core.base_matcher.BaseMatcher`
    :param items: Expected collection of items
    :type items:
    :return: matcher
    :rtype: :py:class:`~hamcrest.core.base_matcher.BaseMatcher`
    """
    return SequenceMapsMatcher(matcher_callable, items)
