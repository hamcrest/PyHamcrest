import re
import unittest
import pytest

from hamcrest.core.selfdescribing import SelfDescribing
from hamcrest.core.string_description import *
from hamcrest.core.localized_description import *


__author__ = "Majority Judgment"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class FakeSelfDescribing(SelfDescribing):
    def describe_to(self, description):
        description.append_text("ENGLISH DESCRIPTION")


class LocalizedDescriptionTest(unittest.TestCase):
    def setUp(self):
        self.description = LocalizedDescription(locale='fr_FR')

    def testLetsSelfDescribingObjectDescribeItself(self):
        self.description.append_description_of(FakeSelfDescribing())
        self.assertEqual("DESCRIPTION FRANÇAISE", str(self.description))

    def testNoL10nWhenDescribesStringInQuotes(self):
        self.description.append_description_of("Butterfly")
        self.assertEqual("'Butterfly'", str(self.description))

    def testNoL10nWhenSelfDescribingObjectInAngleBrackets(self):
        self.description.append_description_of(42)
        self.assertEqual("<42>", str(self.description))

    def testShouldNotAddAngleBracketsIfObjectDescriptionAlreadyHasThem(self):
        self.description.append_description_of(object())
        expected = re.compile("<object object at 0x[0-9a-fA-F]+>")
        self.assertTrue(expected.match(str(self.description)))

    def testDescribeUnicodeStringAsUnicode(self):
        self.description.append_description_of("\u05d0")
        self.assertEqual("'\u05d0'", str(self.description))


# below is a set of things that should append without error to string
# descriptions
@pytest.mark.parametrize("valid_input", (b"bytes", "unicode"))
def test_description_append_valid_input(valid_input):
    desc = LocalizedDescription()
    desc.append(valid_input)
    str(desc)


def test_description_append_invalid_input():
    desc = LocalizedDescription()
    desc.append(chr(239))


if __name__ == "__main__":
    unittest.main()
