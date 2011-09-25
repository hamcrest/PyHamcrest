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


def has_property(name, match=None):
    """Matches if object has a property with a given name whose value satisfies
    a given matcher.

    :param name: The name of the property.
    :param match: Optional matcher to satisfy.

    This matcher determines if the evaluated object has a property with a given
    name. If no such property is found, ``has_property`` is not satisfied.

    If the property is found, its value is passed to a given matcher for
    evaluation. If the ``match`` argument is not a matcher, it is implicitly
    wrapped in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to
    check for equality.

    If the ``match`` argument is not provided, the
    :py:func:`~hamcrest.core.core.isanything.anything` matcher is used so that
    ``has_property`` is satisfied if a matching property is found.

    Examples::

        has_property('name', starts_with('J'))
        has_property('name', 'Jon')
        has_property('name')

    """

    if match is None:
        match = anything()

    return IsObjectWithProperty(name, wrap_shortcut(match))
