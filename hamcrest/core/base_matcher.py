from matcher import Matcher
from string_description import tostring


class BaseMatcher(Matcher):
    """Base class for all Matcher implementations.
    
    Most implementations can just implement _matches, leaving the handling of
    any mismatch description to the matches method. But if it makes more sense
    to generate the mismatch description during the matching, override matches.
    """
    
    def __str__(self):
        return tostring(self)

    def _matches(self, item):
        raise NotImplementedError('_matches')
    
    def matches(self, item, mismatch_description=None):
        match_result = self._matches(item)
        if not match_result and mismatch_description:
            self.describe_mismatch(item, mismatch_description)
        return match_result

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('was ').append_value(item)
