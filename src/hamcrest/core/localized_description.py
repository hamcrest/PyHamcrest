from typing import Any, Iterable

from hamcrest.core.description import Description
from hamcrest.core.locale import get_locale, locale_loader
from hamcrest.core.selfdescribing import SelfDescribing
from hamcrest.core.string_description import StringDescription

__author__ = "Majority Judgment"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


def tostring(selfdescribing: SelfDescribing) -> str:
    """Returns the description of a
    :py:class:`~hamcrest.core.selfdescribing.SelfDescribing` object as a
    localized string.

    :param selfdescribing: The object to be described.
    :returns: The description of the object.
    """
    return str(LocalizedDescription().append_description_of(selfdescribing))


class LocalizedDescription(StringDescription):
    """Implementation of a localized :py:class:`~hamcrest.core.description.Description`
    implementations.
    """

    def __init__(self, locale=None) -> None:
        super().__init__()
        if locale is None:
            locale = get_locale()
        self.locale = locale
        self.locale_map = locale_loader.get_locale_map(self.locale)

    def append_text(self, text: str) -> Description:
        if text in self.locale_map:
            text = self.locale_map[text]
        self.append(text)
        return self
