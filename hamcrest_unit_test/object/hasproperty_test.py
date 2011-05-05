if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')
import sys
print '\n'.join(sys.path)

from hamcrest.library.object.hasproperty import *

from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest
import unittest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

class OnePropertyOldStyle:

    field = 'value'

class OnePropertyNewStyle(object):

    field = 'value'

    def __repr__(self):
        return 'OnePropertyNewStyle'

    def __str__(self):
        return repr(self)

class OverridingOldStyle:

    def __getattr__(self, name):
        if name != 'field':
            raise AttributeError(name)
        return 'value'

class OverridingNewStyleGetAttr(object):

    def __getattr__(self, name):
        if name != 'field':
            raise AttributeError(name)
        return 'value'

class OverridingNewStyleGetAttribute(object):

    def __getattr__(self, name):
        if name != 'field':
            raise AttributeError(name)
        return 'value'

class HasPropertyTest(MatcherTest):

    def testHasPropertyWithoutValueMatcher(self):
        self.assert_matches('old-style direct',
                            has_property('field'), OnePropertyOldStyle())
        self.assert_matches('old-style direct',
                            has_property('field'), OnePropertyNewStyle())
        self.assert_matches('old-style direct',
                            has_property('field'), OverridingOldStyle())
        self.assert_matches('old-style direct',
                            has_property('field'), OverridingNewStyleGetAttr())
        self.assert_matches('old-style direct',
                            has_property('field'), OverridingNewStyleGetAttribute())

    def testHasPropertyWithoutValueMatcherNegative(self):
        self.assert_does_not_match('old-style direct',
                            has_property('not_there'), OnePropertyOldStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('not_there'), OnePropertyNewStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('not_there'), OverridingOldStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('not_there'), OverridingNewStyleGetAttr())
        self.assert_does_not_match('old-style direct',
                            has_property('not_there'), OverridingNewStyleGetAttribute())

    def testHasPropertyWithValueMatcher(self):
        self.assert_matches('old-style direct',
                            has_property('field', 'value'), OnePropertyOldStyle())
        self.assert_matches('old-style direct',
                            has_property('field', 'value'), OnePropertyNewStyle())
        self.assert_matches('old-style direct',
                            has_property('field', 'value'), OverridingOldStyle())
        self.assert_matches('old-style direct',
                            has_property('field', 'value'), OverridingNewStyleGetAttr())
        self.assert_matches('old-style direct',
                            has_property('field', 'value'), OverridingNewStyleGetAttribute())

    def testHasPropertyWithValueMatcherNegative(self):
        self.assert_does_not_match('old-style direct',
                            has_property('field', 'not the value'), OnePropertyOldStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('field', 'not the value'), OnePropertyNewStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('field', 'not the value'), OverridingOldStyle())
        self.assert_does_not_match('old-style direct',
                            has_property('field', 'not the value'), OverridingNewStyleGetAttr())
        self.assert_does_not_match('old-style direct',
                            has_property('field', 'not the value'), OverridingNewStyleGetAttribute())

    def testDescription(self):
        self.assert_description("an object with a property 'field' matching ANYTHING",
                                has_property('field'))
        self.assert_description("an object with a property 'field' matching 'value'",
                                has_property('field', 'value'))

    def testDescribeMissingProperty(self):
        self.assert_mismatch_description("<OnePropertyNewStyle> did not have the 'not_there' property",
                                         has_property('not_there'), OnePropertyNewStyle())

    def testDescribePropertyValueMismatch(self):
        self.assert_mismatch_description("property 'field' was 'value'",
                                         has_property('field', 'another_value'), OnePropertyNewStyle())

    def testMismatchDescription(self):
        self.assert_describe_mismatch("<OnePropertyNewStyle> did not have the 'not_there' property",
                                      has_property('not_there'),
                                      OnePropertyNewStyle())

    def testNoMismatchDescriptionOnMatch(self):
        self.assert_no_mismatch_description(has_property('field', 'value'), OnePropertyNewStyle())


if __name__ == '__main__':
    unittest.main()
