from matcher import Matcher
from string_description import tostring


class BaseMatcher(Matcher):
    """Base class for all Matcher implementations."""
    
    def __str__(self):
        return tostring(self)
