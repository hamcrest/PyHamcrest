__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.string_description import StringDescription

import unittest


class MatcherTest(unittest.TestCase):

    def assert_matches(self, message, matcher, arg):
        self.assertTrue(matcher.matches(arg), message)

    def assert_does_not_match(self, message, matcher, arg):
        self.assertFalse(matcher.matches(arg), message)

    def assert_description(self, expected, matcher):
        description = StringDescription()
        description.append_description_of(matcher);
        self.assertEqual(expected, str(description))

    def assert_no_mismatch_description(self, matcher, arg):
        description = StringDescription()
        result = matcher.matches(arg, description)
        self.assertTrue(result, 'Precondition: Matcher should match item')
        self.assertEqual('', str(description),
                        'Expected no mismatch description')

    def assert_mismatch_description(self, expected, matcher, arg):
        description = StringDescription()
        result = matcher.matches(arg, description)
        self.assertFalse(result, 'Precondition: Matcher should not match item')
        self.assertEqual(expected, str(description))

    def assert_describe_mismatch(self, expected, matcher, arg):
        description = StringDescription()
        matcher.describe_mismatch(arg, description)
        self.assertEqual(expected, str(description))
