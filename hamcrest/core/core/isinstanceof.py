__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import BaseMatcher


class IsInstanceOf(BaseMatcher):
    """Tests whether the value is an instance of a class."""

    def __init__(self, the_class):
        if not isinstance(the_class, type):
            raise TypeError('IsInstanceOf requires type')
        self.the_class = the_class

    def _matches(self, item):
        return isinstance(item, self.the_class)

    def describe_to(self, description):
        description.append_text('an instance of ')          \
                    .append_text(self.the_class.__name__)


"""Is the value an instance of a particular type?"""
instance_of = IsInstanceOf  # Can use directly without a function.
