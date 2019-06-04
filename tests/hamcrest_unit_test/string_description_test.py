import six
from hamcrest.core.string_description import *

from hamcrest.core.selfdescribing import SelfDescribing
import re
import pytest
try:
    import unittest2 as unittest
except ImportError:
    import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class FakeSelfDescribing(SelfDescribing):

    def describe_to(self, description):
        description.append_text('DESCRIPTION')


class StringDescriptionTest(unittest.TestCase):

    def setUp(self):
        self.description = StringDescription()

    def testLetsSelfDescribingObjectDescribeItself(self):
        self.description.append_description_of(FakeSelfDescribing())
        self.assertEqual('DESCRIPTION', str(self.description))

    def testDescribesStringInQuotes(self):
        self.description.append_description_of('FOO')
        self.assertEqual("'FOO'", str(self.description))

    def testWrapsNonSelfDescribingObjectInAngleBrackets(self):
        self.description.append_description_of(42)
        self.assertEqual('<42>', str(self.description))

    def testShouldNotAddAngleBracketsIfObjectDescriptionAlreadyHasThem(self):
        self.description.append_description_of(object())
        expected = re.compile("<object object at 0x[0-9a-fA-F]+>")
        self.assertTrue(expected.match(str(self.description)))

    @unittest.skip("Describe unicode strings doesn't malform in Python 3. Six makes this go away anyway :/")
    def testDescribeUnicodeStringAsBytes(self):
        self.description.append_description_of(six.u('\u05d0'))
        self.assertEqual(six.u('\\u05d0'), str(self.description))

    @unittest.skipUnless(six.PY3, "Describe unicode strings only malforms in Python 2")
    def testDescribeUnicodeStringAsUnicode(self):
        self.description.append_description_of(six.u('\u05d0'))
        self.assertEqual(six.u("'\u05d0'"), str(self.description))


# below is a set of things that should append without error to string
# descriptions
@pytest.mark.parametrize('valid_input', ('native', six.b('bytes'), six.u('unicode')))
def test_description_append_valid_input(valid_input):
    desc = StringDescription()
    desc.append(valid_input)
    str(desc)


def test_description_append_invalid_input():
    desc = StringDescription()
    desc.append(chr(239))

if __name__ == "__main__":
    unittest.main()
