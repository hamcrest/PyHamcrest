if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

import unittest

from hamcrest.core.selfdescribing import SelfDescribing
from hamcrest.core.string_description import StringDescription


class FakeSelfDescribing(SelfDescribing):

    def describe_to(self, description):
        description.append_text('DESCRIPTION')

#==============================================================================

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

if __name__ == "__main__":
    unittest.main()
