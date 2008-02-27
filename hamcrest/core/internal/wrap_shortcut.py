from hamcrest.core.base_matcher import Matcher
from hamcrest.core.core.isequal import equal_to


def wrap_shortcut(item):
    if isinstance(item, Matcher):
        return item
    else:
        return equal_to(item)
