PyHamcrest Tutorial
===================

Introduction
------------

Hamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations where
matchers are invaluable, such as UI validation, or data filtering, but it is in
the area of writing flexible tests that matchers are most commonly used. This
tutorial shows you how to use Hamcrest for unit testing.

When writing tests it is sometimes difficult to get the balance right between
overspecifying the test (and making it brittle to changes), and not specifying
enough (making the test less valuable since it continues to pass even when the
thing being tested is broken). Having a tool that allows you to pick out
precisely the aspect under test and describe the values it should have, to a
controlled level of precision, helps greatly in writing tests that are "just
right." Such tests fail when the behavior of the aspect under test deviates
from the expected behavior, yet continue to pass when minor, unrelated changes
to the behaviour are made.


My first Hamcrest test
----------------------

We'll start by writing a very simple PyUnit test, but instead of using PyUnit's
``assertEqual`` function, we'll use Hamcrest's ``assert_that`` construct and
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
-------------------------

Hamcrest comes with a library of useful matchers. Here are some of the most important ones.

* Core

  * ``anything`` - always matches, useful if you don't care what the object under test is
  * ``described_as`` - decorator to adding custom failure description
  * ``is_`` - decorator to improve readability - see "Syntactic sugar", below

* Logical

  * ``all_of`` - matches if all matchers match, short circuits (like Python &&)
  * ``any_of`` - matches if any matchers match, short circuits (like Python ||)
  * ``is_not`` - matches if the wrapped matcher doesn't match and vice versa

* Object

  * ``equal_to`` - tests object equality using ``==``
  * ``has_length`` - tests whether len(item) satisfies a given matcher
  * ``has_string`` - tests whether str(item) satisfies another matcher
  * ``instance_of`` - tests type
  * ``none``, ``not_none`` - tests for None
  * ``same_instance`` - tests object identity

* Sequences

  * ``has_entry``, ``has_key``, ``has_value`` - tests that a dictionary contains an entry, key or value
  * ``has_item``, ``has_items`` - tests that a sequence contains elements

* Number

  * ``close_to`` - tests that numeric values are close to a given value
  * ``greater_than``, ``greater_than_or_equal_to``, ``less_than``, ``less_than_or_equal_to`` - tests ordering

* Text

  * ``equal_to_ignoring_case`` - tests string equality ignoring case
  * ``equal_to_ignoring_whitespace`` - test strings equality ignoring differences in runs of whitespace
  * ``contains_string``, ``ends_with``, ``starts_with`` - tests string matching


Syntactic sugar
---------------

Hamcrest strives to make your tests as readable as possible. For example, the
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
