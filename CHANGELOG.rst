2.0.3 (2021-12-12)
------------------
 
  Features ^^^^^^^^

  - * Adds the tests to the sdist. Fixed by #150

`#141 <https://github.com/hamcrest/PyHamcrest/issues/141>`_
 - * Update the CI to test Python 3.10

`#160 <https://github.com/hamcrest/PyHamcrest/issues/160>`_
 - * Add pretty string representation for matchers objects

`#170 <https://github.com/hamcrest/PyHamcrest/issues/170>`_

  
 Bugfixes ^^^^^^^^

  - * Test coverage is now submitted to codecov.io.

    Fixed by #150

`#135 <https://github.com/hamcrest/PyHamcrest/issues/135>`_
 - Change to the ``has_entry()`` matcher - if exactly one key matches, but the value does not, report only the mismatching
  value.

  Fixed by #157

`#156 <https://github.com/hamcrest/PyHamcrest/issues/156>`_
 - * Fix is_() type annotations

`#180 <https://github.com/hamcrest/PyHamcrest/issues/180>`_

  
 Misc ^^^^

 - `#150 <https://github.com/hamcrest/PyHamcrest/issues/150>`_, `#159 <https://github.com/hamcrest/PyHamcrest/issues/159>`_, `#162 <https://github.com/hamcrest/PyHamcrest/issues/162>`_, `#163 <https://github.com/hamcrest/PyHamcrest/issues/163>`_, `#166 <https://github.com/hamcrest/PyHamcrest/issues/166>`_, `#175 <https://github.com/hamcrest/PyHamcrest/issues/175>`_

  
   ----


Changelog
=========

Version 2.0.2
-------------

Various type hint bug fixes.

Version 2.0.1
-------------

* Make hamcrest package PEP 561 compatible, i.e. supply type hints for external use.

Version 2.0.0
-------------

Drop formal support for 2.x
Drop formal support for 3.x < 3.5

Fix #128 - raises() grows support for additional matchers on exception object.

* Made has_properties() report all mismatches, not just the first.
* Silence warnings.
* Type fixes.
* Remove obsolete dependencies.

Version 1.10.1
--------------

Add support up to Python 3.8

Fix #66 - deprecate contains() in favour of contains_exactly().
Fix #72 - make has_properties mismatch description less verbose by adding option to AllOf not to include matcher description in its mismatch messages.
Fix #82 - include exception details in mismatch description.

Version 1.9.0
-------------

Drop formal support for 2.x < 2.7
Drop formal support for 3.x < 3.4

Fix #62 - Return result of a deferred call

Version 1.8.5
-------------

Fix #56 - incorrect handling of () in is_ matcher
Fix #60 - correct calling API call with args

Version 1.8.4
-------------

* Fix #54 - Make instance_of work with tuple like isinstance and unittest's assertIsInstance

Version 1.8.3
-------------

* Fix #52 - bad handling when reporting mismatches for byte arrays in Python 3

Version 1.8.2
-------------

* [Bug] Fix unicode syntax via u() introduction (puppsman)

Version 1.8.1
-------------

* Added not_ alias for is_not [Matteo Bertini]
* Added doc directory to the sdist [Alex Brandt]

Version 1.8
-----------

* Supported versions
 - Support for Python 2.5 and Jython 2.5 has been dropped. They may still work, but no promises.

* Bug Fixes
 - [#39] is_empty was missing from the global namespace

* New Features
 - Support for numpy numeric values in iscloseto (Alexander Beedie)
 - A matcher targeting exceptions and call results (Per Fagrell)

Version 1.7
-----------

2 Sep 2013 (Version 1.7.2)
* Supported versions
 - As of this version, support for Python 3.1 has been dropped due to no available CI platform.
 - Added support for Python 3.3

* Bug fixes:
 - string_contains_in_order is now used in the test as it would be in an application, and is properly exported. (Romilly Cocking)
 - Fix mismatch description of containing_inanyorder (David Keijser)
 - added import of stringmatches to text/__init__.py (Eric Scheidemantle)
 - added matches_regexp to __all__ list to library/__init__.py (Eric Scheidemantle)

5 Jan 2010 (Version 1.7.1)
* Bug fixes:
 - included a fix by jaimegildesagredo for issue #28 (has_properties was not importable)
 - included a fix by keys for contains_inanyorder

29 Dec 2012
(All changes by Chris Rose unless otherwise noted.)

* New matchers:
 - matches_regexp matches a regular expression in a string.
 - has_properties matches an object with more than one property.
 - is_empty matches any object with length 0.

* Improvements:
 - Can now do matching against old-style classes.
 - Sequence matchers handle generators, as well as actual sequences and
   pseudo-sequences.
 - README enhancements by ming13


Version 1.6
-----------

27 Sep 2011
(All changes by Chris Rose unless otherwise noted.)

* Packaging:
 - Python 3.2 support.

* New matchers:
 - has_property('property_name', value_matcher) matches if object has a property with a given name whose value satisfies a given matcher.

* Improvements:
 - hasEntries supports two new calling conventions:
    has_entries({'key' : value_matcher, 'key_2' : other_value_matcher})
    has_entries(key=value_matcher, key_2=other_value_matcher)
 - Describe Unicode strings by their __repr__. Thanks to: Sebastian Arming
 - Rewrote documentation. (Jon Reid)


Version 1.5
-----------

29 Apr 2011
* Packaging:
 - Python 3.1 support. Thanks to: Chris Rose
 - Easier installation with bootstrapping. Thanks to: Chris Rose

* Mock integration:
 - "match_equality" wraps a matcher to define equality in terms of satisfying the matcher. This allows Hamcrest matchers to be used in libraries that are not Hamcrest-aware, such as Michael Foord's mock library. Thanks to: Chris Rose

* New matcher:
 - "string_contains_in_order" matches string containing given list of substrings, in order. Thanks to: Romilly Cocking

* Improved matchers:
 - For consistency, changed "any_of" and "all_of" to implicitly wrap non-matcher values in EqualTo. Thanks to: Chris Rose
 - Changed "sameInstance" mismatch description to omit address when describing
 None.


Version 1.4
-----------

13 Feb 2011
* New matchers:
 - "has_entries" matches dictionary containing key-value pairs satisfying a given list of alternating keys and value matchers.

* "assert_that" can be invoked with a single boolean argument; the reason message is now optional. This is a convenience replacement for assertTrue. Thanks to: Jeong-Min Lee

* Improved descriptions:
 - Reverted 1.3 change: Describe None as "<None>" after all, since it is an object.
 - "is_" no longer says "is ..." in its description, but just lets the inner description pass through.
 - Consistently use articles to begin descriptions, such as "a sequence containing" instead of "sequence containing".


Version 1.3
-----------

04 Feb 2011
* PyHamcrest is now compatible with Python 3! To install PyHamcrest on Python 3:
  - Install the "distribute" package, http://pypi.python.org/pypi/distribute
  - Run "python3 setup.py install"
  Unit tests are not converted by the install procedure. Run "2to3 -nw ." separately to convert them. You may discover import statements in the __init__.py files (and one in core/base_description.py) that need dot prefixes.
  Thanks to: Jeong-Min Lee

* Improved descriptions and mismatch descriptions of several matchers, including:
  - Fixed "contains" and "contains_inanyorder" to describe mismatch if item is not a sequence.
  - Fixed "described_as" to use nested matcher to generate mismatch description.
  - "same_instance" is more readable, and includes object memory addresses.
  - If object has a length, "has_length" mismatch describes actual length.
  - Describe None as "None" instead of "<None>".
  - Don't wrap angle brackets around a description that already has them.
  - Improved readability of several matchers.


Version 1.2.1
-------------

04 Jan 2011
* Fixed "assert_that" to describe the diagnosis of the mismatch, not just the
mismatched value. PyHamcrest will now give even more useful information.

* Expanded BaseDescription.append_description_of to handle all types of values, not just self-describing values.

* Deprecated:
 - Description.append_value no longer needed; call append_description_of instead.
 - BaseDescription.append_value_list no longer needed; call append_list instead.
 - SelfDescribingValue no longer needed.

1.2.1 fixes to 1.2:
- Corrected manifest so install works. Thanks to: Jeong-Min Lee


Version 1.1
-----------

28 Dec 2010
* New matchers:
  - "contains" matches sequence containing matching items in order.
  - "contains_inanyorder" matches sequence containing matching items in any order.

* Added Sphinx documentation support.


Version 1.0
-----------

04 Dec 2010
* First official release
* Text matchers now support Unicode strings

15 Jan 2008
* Initial submission
