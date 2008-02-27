from shortcut_combination import ShortcutCombination


class AllOf(ShortcutCombination):
    """Calculates the logical conjunction of two matchers. Evaluation is
    shortcut, so that the second matcher is not called if the first matcher
    returns False.
    """
    
    def __init__(self, *matchers):
        super(AllOf, self).__init__(*matchers)
    
    def matches(self, item):
        return self._matches(item, False)
    
    def describe_to(self, description):
        self._describe_to(description, 'and')


all_of = AllOf
