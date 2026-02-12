import sys

sys.path.append("..")

from hamcrest import *
import unittest


class ExampleWithDeferAssert(unittest.TestCase):
    def testUsingDeferAssertThat(self):
        with DeferAssertContextManager() as da:
            da.assert_that("xx", is_("xx"))


if __name__ == "__main__":
    unittest.main()
