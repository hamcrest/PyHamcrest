import sys

sys.path.append("..")

from hamcrest import *
import unittest


class ExampleWithAssertThat(unittest.TestCase):
    def testUsingAssertThat(self):
        assert_that("xx", is_("xx"))
        assert_that("yy", is_not("xx"))
        assert_that("i like cheese", contains_string("cheese"))

    def testCanAlsoSupplyDescriptiveReason(self):
        assert_that("xx", is_("xx"), "description")

    def testCanAlsoAssertPlainBooleans(self):
        assert_that(True, "This had better not fail")


if __name__ == "__main__":
    unittest.main()
