class Description(object):
    """A description of a Matcher.
    
    A Matcher will describe itself to a description which can later be used for
    reporting.
    
    """

    def append_text(self, text):
        """Appends some plain text to the description."""
        raise NotImplementedError('append_text')

    def append_description_of(self, value):
        """Appends the description of a SelfDescribing value to this
        description.
        """
        raise NotImplementedError('append_description_of')

    def append_value(self, value):
        """Appends an arbitary value to the description."""
        raise NotImplementedError('append_value')
