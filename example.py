from hamcrest import *
import unittest


class ExampleWithAssertThat(unittest.TestCase):
    def testUsingAssertThat(self):
        assert_that('xx', is_('xx'))
        assert_that('yy', is_(not_('xx')))
        assert_that('i like cheese', containsstring('cheese'))


if __name__ == '__main__':
    unittest.main()
