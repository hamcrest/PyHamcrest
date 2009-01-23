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
    
    def assert_no_mismatch_description(self, matcher, arg):
        description = StringDescription()
        result = matcher.matches(arg, description)
        self.assertTrue(result, 'Precondition: Matcher should match item')
        self.assertEquals('', str(description),
                        'Expected no mismatch description')
        
    def assert_mismatch_description(self, expected, matcher, arg):
        description = StringDescription()
        result = matcher.matches(arg, description)
        self.assertFalse(result, 'Precondition: Matcher should not match item')
        self.assertEquals(expected, str(description),
                        'Expected mismatch description')
    
    def assert_describe_mismatch(self, expected, matcher, arg):
        description = StringDescription()
        matcher.describe_mismatch(arg, description)
        self.assertEquals(expected, str(description),
                        'Expected mismatch description')
