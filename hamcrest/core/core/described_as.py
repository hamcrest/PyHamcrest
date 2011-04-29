import re

from hamcrest.core.base_matcher import BaseMatcher, Matcher
from isequal import equal_to
from isinstanceof import instance_of

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


ARG_PATTERN = re.compile('%([0-9]+)')


class DescribedAs(BaseMatcher):
    """Provides a custom description to another matcher."""

    def __init__(self, description_template, matcher, *values):
        self.template = description_template
        self.matcher = matcher
        self.values = values

    def matches(self, item, mismatch_description=None):
        return self.matcher.matches(item, mismatch_description)

    def describe_mismatch(self, item, mismatch_description):
        self.matcher.describe_mismatch(item, mismatch_description)

    def describe_to(self, description):
        text_start = 0
        for match in re.finditer(ARG_PATTERN, self.template):
            description.append_text(self.template[text_start:match.start()])
            arg_index = int(match.group()[1:])
            description.append_description_of(self.values[arg_index])
            text_start = match.end()

        if text_start < len(self.template):
            description.append_text(self.template[text_start:])


def described_as(matcher, *values):
    """Wraps an existing matcher and overrides the description when it fails.

    Optional values following the matcher are substituted for %0, %1, etc.

    """
    return DescribedAs(matcher, *values)
