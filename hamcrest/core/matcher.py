__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from selfdescribing import SelfDescribing


class Matcher(SelfDescribing):
    """A matcher over acceptable values.

    A matcher is able to describe itself to give feedback when it fails.

    Matcher implementations should NOT directly implement this protocol.
    Instead, EXTEND the BaseMatcher class, which will ensure that the Matcher
    API can grow to support new features and remain compatible with all Matcher
    implementations.

    """

    def matches(self, item, mismatch_description=None):
        """Evaluates the matcher for argument item.

        If a mismatch is detected and argument mismatch_description is
        provided, it will generate a description of why the matcher has not
        accepted the item.

        """
        raise NotImplementedError('matches')

    def describe_mismatch(self, item, mismatch_description):
        """Generates a description of why the matcher has not accepted the
        item.

        The description will be part of a larger description of why a matching
        failed, so it should be concise.

        This method assumes that matches(item) is False, but will not check
        this.

        """
        raise NotImplementedError('describe_mismatch')
