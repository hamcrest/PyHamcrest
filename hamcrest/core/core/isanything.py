from hamcrest.core.base_matcher import BaseMatcher


class IsAnything(BaseMatcher):
    """A matcher that always returns True."""
    
    def __init__(self, description=None):
        self.description = description
        if not description:
            self.description = 'ANYTHING'

    def matches(self, item):
        return True

    def describe_to(self, description):
        description.append_text(self.description)


anything = IsAnything