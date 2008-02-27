from shortcut_combination import ShortcutCombination


class AnyOf(ShortcutCombination):
    """Calculates the logical disjunction of two matchers. Evaluation is
    shortcut, so that the second matcher is not called if the first matcher
    returns True.
    """
    
    def __init__(self, *matchers):
        super(AnyOf, self).__init__(*matchers)
    
    def matches(self, item):
        return self._matches(item, True)
    
    def describe_to(self, description):
        self._describe_to(description, 'or')


any_of = AnyOf
