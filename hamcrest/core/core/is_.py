__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from isinstanceof import instance_of


class Is(BaseMatcher):
    """Decorates another Matcher, retaining the behavior but allowing tests to
    be slightly more expressive.

    For example::

        assert_that(cheese, equal_to(smelly))

    vs. ::

        assert_that(cheese, is_(equal_to(smelly)))

    """

    def __init__(self, matcher):
        self.matcher = matcher

    def _matches(self, item):
        return self.matcher.matches(item)

    def describe_to(self, description):
        description.append_text('is ').append_description_of(self.matcher)


def wrap_value_or_type(x):
    if isinstance(x, type):
        return instance_of(x)
    else:
        return wrap_matcher(x)


def is_(x):
    """Decorates an item, providing shortcuts to the frequently used
    expressions ``is_(equal_to(x))`` and ``is_(instance_of(x))``.

    For example::

        assert_that(cheese, is_(equal_to(smelly)))

    vs. ::

        assert_that(cheese, is_(smelly))

    Also::

        assert_that(cheese, is_(instance_of(Cheddar)))

    vs. ::

        assert_that(cheese, is_(Cheddar))

    """
    return Is(wrap_value_or_type(x))
