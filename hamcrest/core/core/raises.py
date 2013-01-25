import re
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Per Fagrell"
__copyright__ = "Copyright 2013 hamcrest.org"
__license__ = "BSD, see License.txt"


class Raises(BaseMatcher):
    def __init__(self, expected, pattern=None):
        self.pattern = pattern
        self.expected = expected
        self.actual = None

    def _matches(self, function):
        if not callable(function):
            return False

        try:
            function()
        except Exception as err:
            self.actual = err

            if isinstance(self.actual, self.expected):
                if self.pattern is not None:
                    return re.search(self.pattern, str(self.actual)) is not None
                return True
        return False

    def describe_to(self, description):
        description.append_text('Expected %s' % self.expected)

    def describe_mismatch(self, item, description):
        if not callable(item):
            description.append_text('%s is not callable' % item)
            return

        if self.actual is None:
            description.append_text('No exception raised.')
        elif isinstance(self.actual, self.expected) and self.pattern is not None:
            description.append_text('Correct assertion type raised, but the expected pattern ("%s") not found.' % self.pattern)
            description.append_text('\n          message was: "%s"' % str(self.actual))
        else:
            description.append_text('%s was raised instead' % type(self.actual))


def raises(exception, pattern=None):
    """Matches if the called function raised the expected exception.

    :param exception:  The class of the expected exception
    :param pattern:    Optional regular expression to match exception message.

    Expects the actual to be wrapped by using :py:func:`~hamcrest.core.core.raises.calling`,
    or a callable taking no arguments.
    Optional argument pattern should be a string containing a regular expression.  If provided,
    the string representation of the actual exception - e.g. `str(actual)` - must match pattern.

    Examples::

        assert_that(calling(int).with_('q'), raises(TypeError))
        assert_that(calling(parse, broken_input), raises(ValueError))
    """
    return Raises(exception, pattern)


class DelayedCall(object):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.func(*self.args, **self.kwargs)

    def with_(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self


def calling(func, *args, **kwargs):
    """Wrapper for function call that delays the actual execution so that
    :py:func:`~hamcrest.core.core.raises.raises` matcher can catch any thrown exception.

    :param func: The function or method to be called
    :param \*args: The positional arguments to pass to the function or method
    :param \*\*kwargs: The keyword arguments to pass to the function or method

    The arguments can either be provided directly along with the function or you can call
    the `with_` function on the returned object as a for of syntactic sugar::

           calling(my_method).with_(arguments, and_='keywords')
    """
    return DelayedCall(func, *args, **kwargs)
