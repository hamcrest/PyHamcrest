from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
import re

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class StringMatchesPattern(BaseMatcher):

    def __init__(self, pattern):
        self.pattern = pattern

    def describe_to(self, description):
        description.append_text("a string matching '") \
                                   .append_text(self.pattern.pattern) \
                                   .append_text("'")

    def _matches(self, item):
        return self.pattern.search(item) is not None


def matches_regexp(pattern):
    if isinstance(pattern, basestring):
        pattern = re.compile(pattern)

    return StringMatchesPattern(pattern)
