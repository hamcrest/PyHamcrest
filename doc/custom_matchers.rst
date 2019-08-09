Writing Custom Matchers
=======================

PyHamcrest comes bundled with lots of useful matchers, but you'll probably find
that you need to create your own from time to time to fit your testing needs.
This commonly occurs when you find a fragment of code that tests the same set
of properties over and over again (and in different tests), and you want to
bundle the fragment into a single assertion. By writing your own matcher you'll
eliminate code duplication and make your tests more readable!

Let's write our own matcher for testing if a calendar date falls on a Saturday.
This is the test we want to write::

    def testDateIsOnASaturday(self):
        d = datetime.date(2008, 04, 26)
        assert_that(d, is_(on_a_saturday()))

And here's the implementation::

    from hamcrest.core.base_matcher import BaseMatcher
    from hamcrest.core.helpers.hasmethod import hasmethod

    class IsGivenDayOfWeek(BaseMatcher):

        def __init__(self, day):
            self.day = day  # Monday is 0, Sunday is 6

        def _matches(self, item):
            if not hasmethod(item, 'weekday'):
                return False
            return item.weekday() == self.day

        def describe_to(self, description):
            day_as_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday']
            description.append_text('calendar date falling on ')    \
                       .append_text(day_as_string[self.day])

    def on_a_saturday():
        return IsGivenDayOfWeek(5)

For our Matcher implementation we implement the
:py:meth:`~hamcrest.core.base_matcher.BaseMatcher._matches` method - which
calls the ``weekday`` method after confirming that the argument (which may not
be a date) has such a method - and the
:py:func:`~hamcrest.core.selfdescribing.SelfDescribing.describe_to` method -
which is used to produce a failure message when a test fails. Here's an example
of how the failure message looks::

    assert_that(datetime.date(2008, 04, 06), is_(on_a_saturday()))

fails with the message::

    AssertionError:
    Expected: is calendar date falling on Saturday
         got: <2008-04-06>

Let's say this matcher is saved in a module named ``isgivendayofweek``. We
could use it in our test by importing the factory function ``on_a_saturday``::

    from hamcrest import *
    import unittest
    from isgivendayofweek import on_a_saturday

    class DateTest(unittest.TestCase):
        def testDateIsOnASaturday(self):
            d = datetime.date(2008, 04, 26)
            assert_that(d, is_(on_a_saturday()))

    if __name__ == '__main__':
        unittest.main()

Even though the ``on_a_saturday`` function creates a new matcher each time it
is called, you should not assume this is the only usage pattern for your
matcher. Therefore you should make sure your matcher is stateless, so a single
instance can be reused between matches.

If you need your matcher to provide more details in case of a mismatch, you
can override the :py:meth:`~hamcrest.core.base_matcher.BaseMatcher.describe_mismatch`
method. For example, if we added this
:py:meth:`~hamcrest.core.base_matcher.BaseMatcher.describe_mismatch` implementation
to our ``IsGivenDayOfWeek`` matcher::

    def describe_mismatch(self, item, mismatch_description):
        day_as_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday']
        mismatch_description.append_text('got ') \
                            .append_description_of(item) \
                            .append_text(' which is a ') \
                            .append_text(day_as_string[item.weekday()])

Our matcher would now give the message::

    AssertionError:
    Expected: is calendar date falling on Saturday
         got: <2008-04-06> which is a Sunday


Occasionally, you might also need your matcher to explain why it matched successfully.
For example, if your matcher is wrapped by a :py:meth:`~hamcrest.core.core.isnot.is_not`
matcher, the ``is_not`` matcher can only explain its mismatches by understanding why your
matcher succeeded. In this case, your matcher can implement
:py:meth:`~hamcrest.core.base_matcher.BaseMatcher.describe_match`.
