from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class NeverMatch(BaseMatcher):

    mismatch_description = "NEVERMATCH"

    def matches(self, item, mismatch_description=None):
        if mismatch_description:
            self.describe_mismatch(item, mismatch_description)
        return False

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text(NeverMatch.mismatch_description)
