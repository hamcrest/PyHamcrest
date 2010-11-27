__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from description import Description
from internal.selfdescribingvalue import SelfDescribingValue


class BaseDescription(Description):

    def append_text(self, text):
        self.append(text)
        return self

    def append_description_of(self, value):
        value.describe_to(self)
        return self

    def append_value(self, value):
        if isinstance(value, str):
            self.append_string_in_python_syntax(value)
        else:
            self.append('<')
            self.append(str(value))
            self.append('>')
        return self

    def append_value_list(self, start, separator, end, list):
        return self.append_list(start, separator, end,
                                map(SelfDescribingValue, list))

    def append_list(self, start, separator, end, list):
        separate = False

        self.append(start)
        for item in list:
            if separate: self.append(separator)
            self.append_description_of(item)
            separate = True
        self.append(end)
        return self

    def append(self, string):
        """Append the string to the description."""
        raise NotImplementedError('append')

    def append_string_in_python_syntax(self, string):
        self.append("'")
        for ch in string:
            self.append(character_in_python_syntax(ch))
        self.append("'")


def character_in_python_syntax(ch):
    if ch == "'":
        return "\'"
    elif ch == '\n':
        return '\\n'
    elif ch == '\r':
        return '\\r'
    elif ch == '\t':
        return '\\t'
    else:
        return ch
