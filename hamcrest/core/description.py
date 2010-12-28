__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

class Description(object):
    """A description of a :py:class:`~hamcrest.core.matcher.Matcher`.

    A :py:class:`~hamcrest.core.matcher.Matcher` will describe itself to a
    description which can later be used for reporting.

    """

    def append_text(self, text):
        """Appends some plain text to the description.

        :returns: ``self``, for chaining

        """
        raise NotImplementedError('append_text')

    def append_description_of(self, value):
        """Appends the description of a
        :py:class:`~hamcrest.core.selfdescribing.SelfDescribing` value to this
        description.

        :returns: ``self``, for chaining

        """
        raise NotImplementedError('append_description_of')

    def append_value(self, value):
        """Appends an arbitary value to the description.

        :returns: ``self``, for chaining

        """
        raise NotImplementedError('append_value')
