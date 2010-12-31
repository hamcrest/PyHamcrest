* [Full documentation](http://packages.python.org/PyHamcrest)
* [Latest package](http://pypi.python.org/pypi/PyHamcrest)
* [Latest sources](https://github.com/jonreid/PyHamcrest)
* [Hamcrest information](http://code.google.com/p/hamcrest)


Introduction
============

PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations where
matchers are invaluable, such as UI validation, or data filtering, but it is in
the area of writing flexible tests that matchers are most commonly used. This
tutorial shows you how to use PyHamcrest for unit testing.

When writing tests it is sometimes difficult to get the balance right between
overspecifying the test (and making it brittle to changes), and not specifying
enough (making the test less valuable since it continues to pass even when the
thing being tested is broken). Having a tool that allows you to pick out
precisely the aspect under test and describe the values it should have, to a
controlled level of precision, helps greatly in writing tests that are "just
right." Such tests fail when the behavior of the aspect under test deviates
from the expected behavior, yet continue to pass when minor, unrelated changes
to the behaviour are made.


My first PyHamcrest test
========================

We'll start by writing a very simple PyUnit test, but instead of using PyUnit's
``assertEqual`` method, we'll use PyHamcrest's ``assert_that`` construct and
the standard set of matchers::

    from hamcrest import *
    import unittest

    class BiscuitTest(unittest.TestCase):
        def testEquals(self):
            theBiscuit = Biscuit('Ginger')
            myBiscuit = Biscuit('Ginger')
            assert_that(theBiscuit, equal_to(myBiscuit))

    if __name__ == '__main__':
        unittest.main()

The ``assert_that`` function is a stylized sentence for making a test
assertion. In this example, the subject of the assertion is the object
``theBiscuit``, which is the first method parameter. The second method
parameter is a matcher for ``Biscuit`` objects, here a matcher that checks one
object is equal to another using the Python ``==`` operator. The test passes
since the ``Biscuit`` class defines an ``__eq__`` method.

If you have more than one assertion in your test you can include an identifier
for the tested value in the assertion::

    assert_that(theBiscuit.getChocolateChipCount(), equal_to(10), 'chocolate chips')
    assert_that(theBiscuit.getHazelnutCount(), equal_to(3), 'hazelnuts')

As a convenience, assert_that can also be used to verify a boolean condition::

    assert_that(theBiscuit.isCooked(), 'cooked')

This is equivalent to the ``assert_`` method of unittest.TestCase, but because
it's a standalone function, it offers greater flexibility in test writing.


A tour of common matchers
=========================

PyHamcrest comes with a library of useful matchers. Here are some of the most
important ones.

* Core

  * ``anything`` - always matches, useful if you don't care what the object
    under test is
  * ``described_as`` - decorator to adding custom failure description
  * ``is_`` - decorator to improve readability - see `Syntactic sugar`, below

* Logical

  * ``all_of`` - matches if all matchers match, short circuits (like Python
    ``and``)
  * ``any_of`` - matches if any matchers match, short circuits (like Python
    ``or``)
  * ``is_not`` - matches if the wrapped matcher doesn't match and vice versa

* Object

  * ``equal_to`` - tests object equality using ``==``
  * ``has_length`` - tests whether ``len(item)`` satisfies a given matcher
  * ``has_string`` - tests whether ``str(item)`` satisfies another matcher
  * ``instance_of`` - tests type
  * ``none``, ``not_none`` - tests for ``None``
  * ``same_instance`` - tests object identity

* Collection

  * ``has_entry``, ``has_key``, ``has_value`` - tests that a dictionary
    contains an entry, key or value
  * ``has_item``, ``has_items`` - tests that a sequence contains elements

* Number

  * ``close_to`` - tests that numeric values are close to a given value
  * ``greater_than``, ``greater_than_or_equal_to``, ``less_than``,
    ``less_than_or_equal_to`` - tests ordering

* Text

  * ``equal_to_ignoring_case`` - tests string equality ignoring case
  * ``equal_to_ignoring_whitespace`` - test strings equality ignoring
    differences in runs of whitespace
  * ``contains_string``, ``ends_with``, ``starts_with`` - tests string matching


Syntactic sugar
===============

PyHamcrest strives to make your tests as readable as possible. For example, the
``is_`` matcher is a wrapper that doesn't add any extra behavior to the
underlying matcher. The following assertions are all equivalent::

    assert_that(theBiscuit, equal_to(myBiscuit))
    assert_that(theBiscuit, is_(equal_to(myBiscuit)))
    assert_that(theBiscuit, is_(myBiscuit))

The last form is allowed since ``is_(value)`` wraps most non-matcher arguments
with ``equal_to``. But if the argument is a type, it is wrapped with
``instance_of``, so the following are also equivalent::

    assert_that(theBiscuit, instance_of(Biscuit))
    assert_that(theBiscuit, is_(instance_of(Biscuit)))
    assert_that(theBiscuit, is_(Biscuit))


Writing custom matchers
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

For our Matcher implementation we implement the ``_matches`` method - which
calls the ``weekday`` method after confirming that the argument (which may not
be a date) has such a method - and the ``describe_to`` method - which is used
to produce a failure message when a test fails. Here's an example of how the
failure message looks::

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
