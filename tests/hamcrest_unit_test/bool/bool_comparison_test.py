from hamcrest import assert_that, equal_to
from hamcrest.core.string_description import StringDescription
from hamcrest.library.bool import is_false, is_true
from hamcrest_unit_test.matcher_test import MatcherTest


class BoolComparisonTest(MatcherTest):
    def test_true_is_true(self):
        self.assert_matches('Is True', is_true(), True)

    def test_false_is_not_true(self):
        self.assert_does_not_match('False', is_true(), False)

    def test_false_is_false(self):
        self.assert_matches('False', is_false(), False)

    def test_true_is_not_false(self):
        self.assert_does_not_match('True', is_false(), True)

    def test_number_is_not_true(self):
        self.assert_does_not_match('True', is_true(), 1)

    def test_number_is_not_false(self):
        self.assert_does_not_match('False', is_false(), 1)

    def test_is_true_description(self):
        description = StringDescription()
        is_true().describe_to(description)
        assert_that(str(description), equal_to('True'))

    def test_is_false_description(self):
        description = StringDescription()
        is_false().describe_to(description)
        assert_that(str(description), equal_to('False'))
