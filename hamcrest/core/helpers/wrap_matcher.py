__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.base_matcher import Matcher
from hamcrest.core.core.isequal import equal_to


def wrap_matcher(x):
    """Wraps argument in a matcher, if necessary.

    :returns: the argument as-is if it is already a matcher, otherwise wrapped
        in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher.

    """
    if isinstance(x, Matcher):
        return x
    else:
        return equal_to(x)
