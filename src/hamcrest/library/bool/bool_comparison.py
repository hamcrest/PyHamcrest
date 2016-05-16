from hamcrest.core.base_matcher import BaseMatcher


class IsABool(BaseMatcher):
    def __init__(self, boolean_value):
        self.boolean_value = boolean_value

    def describe_to(self, description):
        description.append_text(str(self.boolean_value))

    def _matches(self, item):
        if not isinstance(item, bool):
            return False
        return item == self.boolean_value


def is_true():
    return IsABool(True)


def is_false():
    return IsABool(False)
