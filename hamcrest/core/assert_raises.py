__author__ = "Per Fagrell"
__copyright__ = "Copyright 2012 hamcrest.org"
__license__ = "BSD, see License.txt"
__unittest = True

WRONG_EXCEPTION_TEXT = """
Expected: %s raised
     but: %s raised [%s]
"""

NO_EXCEPTION_TEXT = """
Expected: %s raised
     but: No exception raised
"""


def assert_raises(exception, function, *args, **kwargs):
    """Asserts that calling function with the provided arguments causes
    an exception of type *exception* to be raised.

    :param exception: The type of the expected exception.
    :param function: The function or method be be called.
    :param \*args: The arguments to be passed to function.
    :param \*\*kwargs: The keyword arguments to be passed to function.

    ``assert_raises`` calls the provided function or method with all provided
    arguments and checks that the call causes an exception to be raised and that
    the type of the exception matches the provided type::

        assert_raises(IOError, load_schema, nonexistent_file)

    If either of these criteria are not fulfilled an :py:exc:`AssertionError`
    is raised.
    """
    try:
        function(*args, **kwargs)
    except Exception, e:
        if type(e) != exception:
            description = WRONG_EXCEPTION_TEXT % (exception.__name__, type(e).__name__, str(e))
            raise AssertionError(description)
    else:
        description = NO_EXCEPTION_TEXT % exception.__name__
        raise AssertionError(description)
