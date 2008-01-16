from hamcrest.core.base_matcher import BaseMatcher


class ShortcutCombination(BaseMatcher):

    def __init__(self, *matchers):
        self.matchers = matchers

    def _matches(self, item, shortcut):
        for matcher in self.matchers:
            if matcher.matches(item) == shortcut:
                return shortcut
        return not shortcut

    def _describe_to(self, description, operator):
        description.append_list('(', ' ' + operator + ' ', ')', self.matchers)
