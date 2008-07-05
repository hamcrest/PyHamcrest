from hamcrest.core.base_matcher import BaseMatcher
from isinstanceof import instance_of
from hamcrest.core.internal.wrap_shortcut import wrap_shortcut


class Is(BaseMatcher):
    """Decorates another Matcher, retaining the behavior but allowing tests to
    be slightly more expressive.
    
    For example:  assert_that(cheese, equal_to(smelly))
             vs.  assert_that(cheese, is_(equal_to(smelly)))
    """
    
    def __init__(self, matcher):
        self.matcher = matcher

    def matches(self, item):
        return self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('is ').append_description_of(self.matcher)


def _wrap_shortcut(x):
    if isinstance(x, type):
        return instance_of(x)
    else:
        return wrap_shortcut(x)


def is_(x):
    """Decorates an item, providing shortcuts to the frequently used
    expressions is_(equal_to(x)) and is_(instance_of(x)).
    
    For example:  assert_that(cheese, is_(equal_to(smelly)))
             vs.  assert_that(cheese, is_(smelly))
    
    For example:  assert_that(cheese, is_(instance_of(Cheddar)))
             vs.  assert_that(cheese, is_(Cheddar))
    """
    return Is(_wrap_shortcut(x))
