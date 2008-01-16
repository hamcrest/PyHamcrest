class SelfDescribing(object):
    """The ability of an object to describe itself."""

    def describe_to(self, description):
        """Generates a description of the object.
        
        The description may be part of a description of a larger object of
        which this is just a component, so it should be worded appropriately.
        
        """
        raise NotImplementedError('describe_to')
