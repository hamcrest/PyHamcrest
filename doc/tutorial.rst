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
:py:func:`~hamcrest.core.matcher_assert.assert_that` construct and the standard
set of matchers::

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


Asserting Exceptions
--------------------

There's a utility function and matcher available to help you test that
your code has the expected behavior in situations where it should raise
an exception.  The :py:func:`~hamcrest.core.core.raises.calling`
function wraps a callable, and then allows you to set arguments to be
used in a call to the wrapped callable.  This, together with the
:py:func:`~hamcrest.core.core.raises.raises` matcher lets you assert
that calling a method with certain arguments causes an exception to be
thrown. It is also possible to provide a regular expression pattern to
the :py:func:`~hamcrest.core.core.raises.raises` matcher allowing you
assure that the right issue was found::

    assert_that(calling(parse, bad_data), raises(ValueError))

    assert_that(calling(translate).with_(curse_words), raises(LanguageError, "\w+very naughty"))

    assert_that(broken_function, raises(Exception))

    # This will fail and complain that 23 is not callable
    # assert_that(23, raises(IOError))



Predefined matchers
-------------------

PyHamcrest comes with a library of useful matchers:

* Object

  * :py:func:`~hamcrest.core.core.isequal.equal_to` - match equal object
  * :py:func:`~hamcrest.library.object.haslength.has_length` - match
    ``len(item)``
  * :py:func:`~hamcrest.library.object.hasproperty.has_property` - match value
    of property with given name
  * :py:func:`~hamcrest.library.object.hasproperty.has_properties` - match an
     object that has all of the given properties.
  * :py:func:`~hamcrest.library.object.hasstring.has_string` - match
    ``str(item)``
  * :py:func:`~hamcrest.core.core.isinstanceof.instance_of` - match object type
  * :py:func:`~hamcrest.core.core.isnone.none`,
    :py:func:`~hamcrest.core.core.isnone.not_none` - match ``None``, or not
    ``None``
  * :py:func:`~hamcrest.core.core.issame.same_instance` - match same object
  * :py:func:`~hamcrest.core.core.raises.calling`,
    :py:func:`~hamcrest.core.core.raises.raises` - wrap a method call and assert
    that it raises an exception

* Number

  * :py:func:`~hamcrest.library.number.iscloseto.close_to` - match number close
    to a given value
  * :py:func:`~hamcrest.library.number.ordering_comparison.greater_than`,
    :py:func:`~hamcrest.library.number.ordering_comparison.greater_than_or_equal_to`,
    :py:func:`~hamcrest.library.number.ordering_comparison.less_than`,
    :py:func:`~hamcrest.library.number.ordering_comparison.less_than_or_equal_to`
    - match numeric ordering

* Text

  * :py:func:`~hamcrest.library.text.stringcontains.contains_string` - match
    part of a string
  * :py:func:`~hamcrest.library.text.stringendswith.ends_with` - match the end
    of a string
  * :py:func:`~hamcrest.library.text.isequal_ignoring_case.equal_to_ignoring_case`
    - match the complete string but ignore case
  * :py:func:`~hamcrest.library.text.isequal_ignoring_whitespace.equal_to_ignoring_whitespace`
    - match the complete string but ignore extra whitespace
  * :py:func:`~hamcrest.library.text.stringstartswith.starts_with` - match the
    beginning of a string
  * :py:func:`~hamcrest.library.text.stringcontainsinorder.string_contains_in_order`
    - match parts of a string, in relative order

* Logical

  * :py:func:`~hamcrest.core.core.allof.all_of` - ``and`` together all matchers
  * :py:func:`~hamcrest.core.core.anyof.any_of` - ``or`` together all matchers
  * :py:func:`~hamcrest.core.core.isanything.anything` - match anything, useful
    in composite matchers when you don't care about a particular value
  * :py:func:`~hamcrest.core.core.isnot.is_not` - negate the matcher
  * :py:func:`~hamcrest.core.core.isnot.not_` - alias of
    :py:func:`~hamcrest.core.core.isnot.is_not` for better readability of negations.

* Sequence

  * :py:func:`~hamcrest.library.collection.issequence_containinginorder.contains`
    - exactly match the entire sequence
  * :py:func:`~hamcrest.library.collection.issequence_containinginanyorder.contains_inanyorder`
    - match the entire sequence, but in any order
  * :py:func:`~hamcrest.library.collection.issequence_containing.has_item` -
    match if given item appears in the sequence
  * :py:func:`~hamcrest.library.collection.issequence_containing.has_items` -
    match if all given items appear in the list, in any order
  * :py:func:`~hamcrest.library.collection.isin.is_in` - match if item appears
    in the given sequence
  * :py:func:`~hamcrest.library.collection.issequence_onlycontaining.only_contains`
    - match if sequence's items appear in given list
  * :py:func:`~hamcrest.library.collection.is_empty.empty`
    - match if the sequence is empty

* Dictionary

  * :py:func:`~hamcrest.library.collection.isdict_containingentries.has_entries`
    - match dictionary with list of key-value pairs
  * :py:func:`~hamcrest.library.collection.isdict_containing.has_entry` - match
    dictionary containing a key-value pair
  * :py:func:`~hamcrest.library.collection.isdict_containingkey.has_key` -
    match dictionary with a key
  * :py:func:`~hamcrest.library.collection.isdict_containingvalue.has_value` -
    match dictionary with a value

* Decorator

  * :py:func:`~hamcrest.core.core.described_as.described_as` - give the matcher
    a custom failure description
  * :py:func:`~hamcrest.core.core.is_.is_` - decorator to improve readability -
    see :ref:`sugar`, below

The arguments for many of these matchers accept not just a matching value, but
another matcher, so matchers can be composed for greater flexibility. For
example, ``only_contains(less_than(5))`` will match any sequence where every
item is less than 5.


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

(Note that PyHamcrest's ``is_`` matcher is unrelated to Python's ``is``
operator. The matcher for object identity is
:py:func:`~hamcrest.core.core.issame.same_instance`.)
