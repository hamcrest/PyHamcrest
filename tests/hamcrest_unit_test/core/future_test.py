import sys

import pytest
import asyncio
from hamcrest import has_properties
from hamcrest.core.core.future import resolved, future_raising
from hamcrest_unit_test.matcher_test import MatcherTest

if __name__ == "__main__":
    sys.path.insert(0, "..")
    sys.path.insert(0, "../..")


__author__ = "David Keijser"
__copyright__ = "Copyright 2023 hamcrest.org"
__license__ = "BSD, see License.txt"


async def no_exception(*args, **kwargs):
    return


async def raise_exception(*args, **kwargs):
    raise AssertionError(str(args) + str(kwargs))


async def raise_exception_with_properties(**kwargs):
    err = AssertionError("boom")
    for k, v in kwargs.items():
        setattr(err, k, v)
    raise err


# From python 3.8 this could be simplified by using unittest.IsolatedAsyncioTestCase
class FutureExceptionTest(MatcherTest):
    def testMatchesIfFutureHasTheExactExceptionExpected(self):
        async def test():
            self.assert_matches(
                "Right exception",
                future_raising(AssertionError),
                await resolved(raise_exception()),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchIfActualIsNotAFuture(self):
        async def test():
            self.assert_does_not_match("Not a future", future_raising(TypeError), 23)

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchIfFutureIsNotDone(self):
        future = asyncio.Future()
        self.assert_does_not_match("Unresolved future", future_raising(TypeError), future)

    def testDoesNotMatchIfFutureIsCancelled(self):
        future = asyncio.Future()
        future.cancel()
        self.assert_does_not_match("Cancelled future", future_raising(TypeError), future)

    @pytest.mark.skipif(
        not (3, 0) <= sys.version_info < (3, 7), reason="Message differs between Python versions"
    )
    def testDoesNotMatchIfFutureHasTheWrongExceptionTypePy3(self):
        async def test():
            self.assert_does_not_match(
                "Wrong exception", future_raising(IOError), await resolved(raise_exception())
            )
            expected_message = (
                "AssertionError('(){}',) of type <class 'AssertionError'> was raised instead"
            )
            self.assert_mismatch_description(
                expected_message, future_raising(TypeError), await resolved(raise_exception())
            )

        asyncio.get_event_loop().run_until_complete(test())

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="Message differs between Python versions")
    def testDoesNotMatchIfFutureHasTheWrongExceptionTypePy37(self):
        async def test():
            self.assert_does_not_match(
                "Wrong exception", future_raising(IOError), await resolved(raise_exception())
            )
            expected_message = (
                "AssertionError('(){}') of type <class 'AssertionError'> was raised instead"
            )
            self.assert_mismatch_description(
                expected_message, future_raising(TypeError), await resolved(raise_exception())
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testMatchesIfFutureHasASubclassOfTheExpectedException(self):
        async def test():
            self.assert_matches(
                "Subclassed Exception",
                future_raising(Exception),
                await resolved(raise_exception()),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchIfFutureDoesNotHaveException(self):
        async def test():
            self.assert_does_not_match(
                "No exception", future_raising(ValueError), await resolved(no_exception())
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchExceptionIfRegularExpressionDoesNotMatch(self):
        async def test():
            self.assert_does_not_match(
                "Bad regex",
                future_raising(AssertionError, "Phrase not found"),
                await resolved(raise_exception()),
            )
            self.assert_mismatch_description(
                '''Correct assertion type raised, but the expected pattern ("Phrase not found") not found. Exception message was: "(){}"''',
                future_raising(AssertionError, "Phrase not found"),
                await resolved(raise_exception()),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testMatchesRegularExpressionToStringifiedException(self):
        async def test():
            self.assert_matches(
                "Regex",
                future_raising(AssertionError, "(3, 1, 4)"),
                await resolved(raise_exception(3, 1, 4)),
            )

            self.assert_matches(
                "Regex",
                future_raising(AssertionError, r"([\d, ]+)"),
                await resolved(raise_exception(3, 1, 4)),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testMachesIfExceptionMatchesAdditionalMatchers(self):
        async def test():
            self.assert_matches(
                "Properties",
                future_raising(AssertionError, matching=has_properties(prip="prop")),
                await resolved(raise_exception_with_properties(prip="prop")),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchIfAdditionalMatchersDoesNotMatch(self):
        async def test():
            self.assert_does_not_match(
                "Bad properties",
                future_raising(AssertionError, matching=has_properties(prop="prip")),
                await resolved(raise_exception_with_properties(prip="prop")),
            )
            self.assert_mismatch_description(
                '''Correct assertion type raised, but an object with a property 'prop' matching 'prip' not found. Exception message was: "boom"''',
                future_raising(AssertionError, matching=has_properties(prop="prip")),
                await resolved(raise_exception_with_properties(prip="prop")),
            )

        asyncio.get_event_loop().run_until_complete(test())

    def testDoesNotMatchIfNeitherPatternOrMatcherMatch(self):
        async def test():
            self.assert_does_not_match(
                "Bad pattern and properties",
                future_raising(
                    AssertionError, pattern="asdf", matching=has_properties(prop="prip")
                ),
                await resolved(raise_exception_with_properties(prip="prop")),
            )
            self.assert_mismatch_description(
                '''Correct assertion type raised, but the expected pattern ("asdf") and an object with a property 'prop' matching 'prip' not found. Exception message was: "boom"''',
                future_raising(
                    AssertionError, pattern="asdf", matching=has_properties(prop="prip")
                ),
                await resolved(raise_exception_with_properties(prip="prop")),
            )

        asyncio.get_event_loop().run_until_complete(test())
