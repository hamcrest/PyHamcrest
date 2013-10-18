from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class SubstringMatcher(BaseMatcher):

    def __init__(self, substring):
        if not isinstance(substring, basestring):
            raise TypeError(self.__class__.__name__ + ' requires string')
        self.substring = substring

    def describe_to(self, description):
        description.append_text('a string ')                \
                   .append_text(self.relationship())        \
                   .append_text(' ')                        \
                   .append_description_of(self.substring)
