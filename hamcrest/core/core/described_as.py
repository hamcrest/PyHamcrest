import re

from hamcrest.core.base_matcher import BaseMatcher, Matcher
from isequal import equal_to
from isinstanceof import instance_of


ARG_PATTERN = re.compile('%([0-9]+)')

class DescribedAs(BaseMatcher):
    """Provides a custom description to another matcher.
    
    Optional values following the matcher are substituted for %0, %1, etc.

    """
    
    def __init__(self, description_template, matcher, *values):
        self.template = description_template
        self.matcher = matcher
        self.values = values

    def _matches(self, item):
        return self.matcher.matches(item)

    def describe_to(self, description):
        text_start = 0
        for match in re.finditer(ARG_PATTERN, self.template):
            description.append_text(self.template[text_start:match.start()])
            arg_index = int(match.group()[1:])
            description.append_value(self.values[arg_index])
            text_start = match.end()
        
        if text_start < len(self.template):
            description.append_text(self.template[text_start:])


"""Wraps an existing matcher and overrides the description when it fails."""
described_as = DescribedAs  # Can use directly without a function.
