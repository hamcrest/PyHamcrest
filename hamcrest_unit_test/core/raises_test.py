if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.core.core.raises import *

from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest
import unittest

__author__ = "Per Fagrell"
__copyright__ = "Copyright 2013 hamcrest.org"
__license__ = "BSD, see License.txt"


def no_exception(*args, **kwargs):
    return


def raise_exception(*args, **kwargs):
    raise AssertionError(str(args) + str(kwargs))


class RaisesTest(MatcherTest):
    def testMatchesIfFunctionRaisesTheExactExceptionExpected(self):
        self.assert_matches('Right exception',
                            raises(AssertionError),
                            calling(raise_exception))

    def testDoesNotMatchTypeErrorIfActualIsNotCallable(self):
        self.assert_does_not_match('Not callable',
                                   raises(TypeError),
                                   23)

    def testMatchesIfFunctionRaisesASubclassOfTheExpectedException(self):
        self.assert_matches('Subclassed Exception',
                            raises(Exception),
                            calling(raise_exception))

    def testDoesNotMatchIfFunctionDoesNotRaiseException(self):
        self.assert_does_not_match('No exception',
                            raises(ValueError),
                            calling(no_exception))

    def testDoesNotMatchExceptionIfRegularExpressionDoesNotMatch(self):
        self.assert_does_not_match('Bad regex',
                                   raises(AssertionError, "Bananarama"),
                                   calling(raise_exception))

    def testMatchesRegularExpressionToStringifiedException(self):
        self.assert_matches('Regex',
                            raises(AssertionError, "(3, 1, 4)"),
                            calling(raise_exception).with_(3,1,4))

        self.assert_matches('Regex',
                            raises(AssertionError, "([\d, ]+)"),
                            calling(raise_exception).with_(3,1,4))


class CallingTest(unittest.TestCase):
    def testCallingDoesNotImmediatelyExecuteFunction(self):
        try:
            calling(raise_exception)
        except AssertionError:
            self.fail()
        else:
            pass

    def testCallingObjectCallsProvidedFunction(self):
        method = Callable()
        calling(method)()
        self.assertTrue(method.called)

    def testCallingObjectPassesArgsAndKwargs(self):
        method = Callable()
        calling(method, "Banana", 3, keyword1="happy")()

        self.assertEqual(method.args, ("Banana", 3))
        self.assertEqual(method.kwargs, {'keyword1': 'happy'})

    def testCallingWithFunctionReturnsObject(self):
        method = Callable()
        callable = calling(method)
        returned = callable.with_(3, 1, 4, keyword2="bronze")

        self.assertEqual(returned, callable)

    def testCallingWithFunctionSetsArgumentList(self):
        method = Callable()
        calling(method).with_(3, 1, 4, keyword2="bronze")()

        self.assertEqual(method.args, (3, 1, 4))
        self.assertEqual(method.kwargs, {'keyword2': 'bronze'})


class Callable(object):
    def __init__(self):
        self.called = False

    def __call__(self, *args, **kwargs):
        self.called = True
        self.args = args
        self.kwargs = kwargs
