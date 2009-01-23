from hamcrest.core.base_matcher import BaseMatcher


class IsEqualIgnoringWhiteSpace(BaseMatcher):
    """Matches if strings are equal ignoring white space."""

    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError('IsEqualIgnoringWhiteSpace requires string')
        self.original_string = string
        self.stripped_string = stripspace(string)
    
    def _matches(self, item):
        if not isinstance(item, str):
            return False
        return self.stripped_string == stripspace(item)

    def describe_to(self, description):
        description.append_text('equal_to_ignoring_whitespace(')    \
                    .append_value(self.original_string)             \
                    .append_text(')')


def stripspace(string):
    result = ''
    last_was_space = True
    for character in string:
        if character.isspace():
            if not last_was_space:
                result += ' '
            last_was_space = True
        else:
            result += character
            last_was_space = False
    return result.strip()


"""Are the strings equal, ignoring white space?"""
equal_to_ignoring_whitespace = IsEqualIgnoringWhiteSpace    # Can use directly without a function.
