PyHamcrest Tutorial
===================

Introduction
------------

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
------------------------

We'll start by writing a very simple PyUnit test, but instead of using PyUnit's
:py:meth:`~unittest.TestCase.assertEqual` method, we'll use PyHamcrest's
:py:func:`~hamcrest.core.matcher_assert.assert_that` construct and the standard set of matchers::

    from hamcrest import *
    import unittest

    class BiscuitTest(unittest.TestCase):
        def testEquals(self):
            theBiscuit = Biscuit('Ginger')
            myBiscuit = Biscuit('Ginger')
            assert_that(theBiscuit, equal_to(myBiscuit))

    if __name__ == '__main__':
        unittest.main()

The :py:func:`~hamcrest.core.matcher_assert.assert_that` function is a stylized
sentence for making a test assertion. In this example, the subject of the
assertion is the object ``theBiscuit``, which is the first method parameter.
The second method parameter is a matcher for ``Biscuit`` objects, here a
matcher that checks one object is equal to another using the Python ``==``
operator. The test passes since the ``Biscuit`` class defines an ``__eq__``
method.

If you have more than one assertion in your test you can include an identifier
for the tested value in the assertion::

    assert_that(theBiscuit.getChocolateChipCount(), equal_to(10), 'chocolate chips')
    assert_that(theBiscuit.getHazelnutCount(), equal_to(3), 'hazelnuts')

As a convenience, :py:func:`~hamcrest.core.matcher_assert.assert_that` can also
be used to verify a boolean condition::

    assert_that(theBiscuit.isCooked(), 'cooked')

This is equivalent to the :py:meth:`~unittest.TestCase.assert_` method of
:py:class:`unittest.TestCase`, but because it's a standalone function, it
offers greater flexibility in test writing.


A tour of common matchers
-------------------------

PyHamcrest comes with a library of useful matchers. Here are some of the most
important ones.

* Core

  * :py:func:`~hamcrest.core.core.isanything.anything` - always matches, useful
    if you don't care what the object under test is
  * :py:func:`~hamcrest.core.core.described_as.described_as` - decorator to
    add custom failure description
  * :py:func:`~hamcrest.core.core.is_.is_` - decorator to improve readability -
    see :ref:`sugar`, below

* Logical

  * :py:func:`~hamcrest.core.core.allof.all_of` - matches if all matchers
    match, short circuits (like Python ``and``)
  * :py:func:`~hamcrest.core.core.anyof.any_of` - matches if any matchers
    match, short circuits (like Python ``or``)
  * :py:func:`~hamcrest.core.core.isnot.is_not` - matches if the wrapped
    matcher doesn't match and vice versa

* Object

  * :py:func:`~hamcrest.core.core.isequal.equal_to` - tests object equality
    using ``==``
  * :py:func:`~hamcrest.library.object.haslength.has_length` - tests whether
    ``len(item)`` satisfies a given matcher
  * :py:func:`~hamcrest.library.object.hasstring.has_string` - tests whether
    ``str(item)`` satisfies another matcher
  * :py:func:`~hamcrest.core.core.isinstanceof.instance_of` - tests type
  * :py:func:`~hamcrest.core.core.isnone.none`,
    :py:func:`~hamcrest.core.core.isnone.not_none` - tests for ``None``
  * :py:func:`~hamcrest.core.core.issame.same_instance` - tests object identity

* Collection

  * :py:func:`~hamcrest.library.collection.isdict_containing.has_entry`,
    :py:func:`~hamcrest.library.collection.isdict_containingentries.has_entries`,
    :py:func:`~hamcrest.library.collection.isdict_containingkey.has_key`,
    :py:func:`~hamcrest.library.collection.isdict_containingvalue.has_value` -
    tests that a dictionary contains an entry, key or value
  * :py:func:`~hamcrest.library.collection.issequence_containing.has_item`,
    :py:func:`~hamcrest.library.collection.issequence_containinginorder.contains`,
    :py:func:`~hamcrest.library.collection.issequence_containinginanyorder.contains_inanyorder` -
    tests that a sequence contains elements

* Number

  * :py:func:`~hamcrest.library.number.iscloseto.close_to` - tests that numeric
    values are close to a given value
  * :py:func:`~hamcrest.library.number.ordering_comparison.greater_than`,
    :py:func:`~hamcrest.library.number.ordering_comparison.greater_than_or_equal_to`,
    :py:func:`~hamcrest.library.number.ordering_comparison.less_than`,
    :py:func:`~hamcrest.library.number.ordering_comparison.less_than_or_equal_to`
    - tests ordering

* Text

  * :py:func:`~hamcrest.library.text.isequal_ignoring_case.equal_to_ignoring_case`
    - tests string equality ignoring case
  * :py:func:`~hamcrest.library.text.isequal_ignoring_whitespace.equal_to_ignoring_whitespace`
    - test strings equality ignoring differences in runs of whitespace
  * :py:func:`~hamcrest.library.text.stringcontains.contains_string`,
    :py:func:`~hamcrest.library.text.stringendswith.ends_with`,
    :py:func:`~hamcrest.library.text.stringstartswith.starts_with` - tests
    string matching


.. _sugar:

Syntactic sugar
---------------

PyHamcrest strives to make your tests as readable as possible. For example, the
:py:func:`~hamcrest.core.core.is_.is_` matcher is a wrapper that doesn't add
any extra behavior to the underlying matcher. The following assertions are all
equivalent::

    assert_that(theBiscuit, equal_to(myBiscuit))
    assert_that(theBiscuit, is_(equal_to(myBiscuit)))
    assert_that(theBiscuit, is_(myBiscuit))

The last form is allowed since ``is_(value)`` wraps most non-matcher arguments
with :py:func:`~hamcrest.core.core.isequal.equal_to`. But if the argument is a
type, it is wrapped with
:py:func:`~hamcrest.core.core.isinstanceof.instance_of`, so the following are
also equivalent::

    assert_that(theBiscuit, instance_of(Biscuit))
    assert_that(theBiscuit, is_(instance_of(Biscuit)))
    assert_that(theBiscuit, is_(Biscuit))
