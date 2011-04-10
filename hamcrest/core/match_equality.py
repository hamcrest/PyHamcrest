"""Equality matching support; easier to integrate with hamcrest-unaware libraries"""

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"
__unittest = True

from string_description import tostring

class EqualityWrapper(object):

    def __init__(self, matcher):
        self.matcher = matcher

    def __eq__(self, o):
        return self.matcher.matches(o)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return tostring(self.matcher)

def match_equality(matcher):
    """Wrap a matcher in an object that defines equality to an object in terms
    of the matcher.

    This allows matchers to be used in libraries that are not hamcrest aware;
    if they test for equality::

        assert match_equality(matcher) == object

    or ::

        library.method_that_tests_eq(match_equality(matcher))

    One example is integrating with the assert_called_with methods in Michael
    Foord's mock library.

    """
    from helpers.wrap_matcher import wrap_matcher
    return EqualityWrapper(wrap_matcher(matcher))
