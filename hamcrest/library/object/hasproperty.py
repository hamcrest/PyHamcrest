from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core import anything
from hamcrest.core.string_description import StringDescription
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher as wrap_shortcut

__author__ = "Chris Rose"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

class IsObjectWithProperty(BaseMatcher):

    def __init__(self, property_name, value_matcher):
        self.property_name = property_name
        self.value_matcher = value_matcher

    def _matches(self, o):
        if o is None:
            return False

        if not hasattr(o, self.property_name):
            return False

        value = getattr(o, self.property_name)
        return self.value_matcher.matches(value)

    def describe_to(self, description):
        description.append_text("an object with a property '") \
                                        .append_text(self.property_name) \
                                        .append_text("' matching ") \
                                        .append_description_of(self.value_matcher)

    def describe_mismatch(self, item, mismatch_description):
        if item is None:
            mismatch_description.append_text('was None')
            return

        if not hasattr(item, self.property_name):
            mismatch_description.append_value(item) \
                                                    .append_text(' did not have the ') \
                                                    .append_value(self.property_name) \
                                                    .append_text(' property')
            return

        mismatch_description.append_text('property ').append_value(self.property_name).append_text(' ')
        value = getattr(item, self.property_name)
        self.value_matcher.describe_mismatch(value, mismatch_description)

    def __str__(self):
        d = StringDescription()
        self.describe_to(d)
        return str(d)

def has_property(name, value=None):
    """Matches objects that have a property matching the given value matcher.

    :param name: The name of the property that the object must have. If the object
        does not have this property, the matcher will fail.

    :param value: The value to match. If the value is not provided, the
        matcher will match against anything(), which transforms this
        matcher into a property existence check.

    """

    if value is None:
        value = anything()

    return IsObjectWithProperty(name, wrap_shortcut(value))
