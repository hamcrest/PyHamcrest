if __name__ == "__main__":
    import sys
    sys.path.insert(0, '..')

import unittest

from hamcrest.core.base_matcher import *


class TestingBaseMatcher(BaseMatcher):

    def describe_to(self, description):
        description.append_text('SOME DESCRIPTION')


class BaseMatcherTest(unittest.TestCase):

    def testDescribesItselfWithToStr(self):
        matcher = TestingBaseMatcher()
        self.assertEquals('SOME DESCRIPTION', str(matcher))


if __name__ == "__main__":
    unittest.main()
