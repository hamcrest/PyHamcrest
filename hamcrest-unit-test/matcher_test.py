import unittest

from hamcrest.core.string_description import StringDescription


class MatcherTest(unittest.TestCase):

    def assert_matches(self, message, c, arg):
        self.assert_(c.matches(arg), message)

    def assert_does_not_match(self, message, c, arg):
        self.assert_(not c.matches(arg), message)

    def assert_description(self, expected, matcher):
        description = StringDescription()
        description.append_description_of(matcher);
        self.assertEqual(expected, str(description))
