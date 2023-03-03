import unittest

from hamcrest import assert_that, calling, raises


def raise_error(msg):
    raise AssertionError(msg)


class ParensTest(unittest.TestCase):

    def test_literal_parens(self):

        message = 'Message with (parens)'
        assert_that(
            calling(raise_error).with_args(message),
            raises(AssertionError, message)
        )

    def test_parens_in_regex(self):
        assert_that(
            calling(raise_error).with_args('abab'),
            raises(AssertionError, r'(ab)+')
        )
