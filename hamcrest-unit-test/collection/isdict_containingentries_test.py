__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

from hamcrest.library.collection.isdict_containingentries import *

from hamcrest.core.core.isequal import equal_to
from matcher_test import MatcherTest
import unittest


class IsDictContainingEntriesTest(MatcherTest):

    def testMatcherCreationRequiresEvenNumberOfArgs(self):
        self.assertRaises(SyntaxError, has_entries, 'a')

    def testDoesNotMatchNonDictionary(self):
        self.assert_does_not_match('non-dictionary',
                                    has_entries('a', equal_to(1)), object())

    def testMatchesDictionaryContainingSingleKeyWithMatchingValue(self):
        dict = {'a': 1, 'b': 2}
        self.assert_matches('has a:1', has_entries('a', equal_to(1)), dict)
        self.assert_matches('has b:2', has_entries('b', equal_to(2)), dict)
        self.assert_does_not_match('no b:3', has_entries('b', equal_to(3)), dict)
        self.assert_does_not_match('no c:2', has_entries('c', equal_to(2)), dict)

    def testMatchesDictionaryContainingMultipleKeysWithMatchingValues(self):
        dict = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('has a & b',
                        has_entries('a', equal_to(1), 'b', equal_to(2)), dict)
        self.assert_matches('has c & a',
                        has_entries('c', equal_to(3), 'a', equal_to(1)), dict)
        self.assert_does_not_match('no d:3',
                        has_entries('b', equal_to(3), 'd', equal_to(3)), dict)

    def testProvidesConvenientShortcutForMatchingWithIsEqualTo(self):
        dict = {'a': 1, 'b': 2, 'c': 3}
        self.assert_matches('has a & b', has_entries('a', 1, 'b', 2), dict)
        self.assert_matches('has c & a', has_entries('c', 3, 'a', 1), dict)
        self.assert_does_not_match('no d:4', has_entries('b', 3, 'd', 4), dict)

    def testHasReadableDescription(self):
        self.assert_description("a dictionary containing {'a': <1>, 'b': <2>}",
                                has_entries('a', 1, 'b', 2))

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(has_entries('a', 1), {'a': 1})

    def testMismatchDescriptionOfNonDictionaryShowsActualArgument(self):
        self.assert_mismatch_description("was 'bad'", has_entries('a', 1), 'bad')

    def testMismatchDescriptionOfDictionaryWithoutKey(self):
        self.assert_mismatch_description("no 'b' key in <{'a': 1, 'c': 3}>",
                                has_entries('a', 1, 'b', 2), {'a': 1, 'c': 3})

    def testMismatchDescriptionOfDictionaryWithNonMatchingValue(self):
        self.assert_mismatch_description("value for 'a' was <2>",
                                has_entries('a', 1), {'a': 2})

    def testDescribeMismatchOfNonDictionaryShowsActualArgument(self):
        self.assert_describe_mismatch("was 'bad'", has_entries('a', 1), 'bad')

    def testDescribeMismatchOfDictionaryWithoutKey(self):
        self.assert_describe_mismatch("no 'b' key in <{'a': 1, 'c': 3}>",
                                has_entries('a', 1, 'b', 2), {'a': 1, 'c': 3})

    def testDescribeMismatchOfDictionaryWithNonMatchingValue(self):
        self.assert_describe_mismatch("value for 'a' was <2>",
                                has_entries('a', 1), {'a': 2})


if __name__ == '__main__':
    unittest.main()
