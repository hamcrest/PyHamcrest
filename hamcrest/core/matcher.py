from selfdescribing import SelfDescribing


class Matcher(SelfDescribing):
    """A matcher over acceptable values.
    
    A matcher is able to describe itself to give feedback when it fails.
    
    """

    def matches(self, item):
        """Evaluates the matcher for argument item"""
        raise NotImplementedError('matches')
