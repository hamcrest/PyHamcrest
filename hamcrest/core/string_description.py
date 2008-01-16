from base_description import BaseDescription


def tostring(selfdescribing):
    """Returns the description of a SelfDescribing object as a string."""
    return str(StringDescription().append_description_of(selfdescribing))


class StringDescription(BaseDescription):
    """A Description that is stored as a string."""
    
    def __init__(self):
        self.out = ''
    
    def __str__(self):
        """Returns the description."""
        return self.out
    
    def append(self, string):
        self.out += string
