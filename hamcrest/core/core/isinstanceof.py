__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.base_matcher import BaseMatcher


class IsInstanceOf(BaseMatcher):
    """Tests whether the value is an instance of a class."""

    def __init__(self, expected_type):
        if not isinstance(expected_type, type):
            raise TypeError('IsInstanceOf requires type')
        self.expected_type = expected_type

    def _matches(self, item):
        return isinstance(item, self.expected_type)

    def describe_to(self, description):
        description.append_text('an instance of ')              \
                    .append_text(self.expected_type.__name__)


def instance_of(expected_type):
    """Is the value an instance of a particular type?"""
    return IsInstanceOf(expected_type)
