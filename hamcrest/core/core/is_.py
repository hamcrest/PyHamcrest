from hamcrest.core.base_matcher import BaseMatcher
from isinstanceof import instanceof
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class Is(BaseMatcher):
    """Decorates another Matcher, retaining the behavior but allowing tests to
    be slightly more expressive.
    
    For example,
        assert_that(cheese, equalto(smelly))
    vs.
        assert_that(cheese, is(equalto(smelly)))
    """
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, item):
        return self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('is ').append_description_of(self.matcher)


def _wrap_shortcut(item):
    if isinstance(item, type):
        return instanceof(item)
    else:
        return wrap_shortcut(item)


def is_(item):
    return Is(_wrap_shortcut(item))
