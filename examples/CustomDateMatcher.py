import sys
sys.path.append('..')

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

from hamcrest import *
import unittest
import datetime


class IsGivenDayOfWeek(BaseMatcher):
    """Matches dates that fall on a given day of the week."""

    def __init__(self, day):
        self.day = day  # Monday is 0, Sunday is 6

    def _matches(self, item):
        """Test whether item matches."""
        if not hasmethod(item, 'weekday'):
            return False
        return item.weekday() == self.day

    def describe_to(self, description):
        """Describe the matcher."""
        day_as_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday']
        description.append_text('calendar date falling on ')    \
                   .append_text(day_as_string[self.day])


def on_a_saturday():
    """Factory function to generate Saturday matcher."""
    return IsGivenDayOfWeek(5)


class SampleTest(unittest.TestCase):
    def testDateIsOnASaturday(self):
        """Example of successful match."""
        d = datetime.date(2008, 04, 26)
        assert_that(d, is_(on_a_saturday()))

    def testFailsWithMismatchedDate(self):
        """Example of what happens with date that doesn't match."""
        d = datetime.date(2008, 04, 06)
        assert_that(d, is_(on_a_saturday()))

    def testFailsWithNonDate(self):
        """Example of what happens with object that isn't a date."""
        d = 'oops'
        assert_that(d, is_(on_a_saturday()))


if __name__ == '__main__':
    unittest.main()
