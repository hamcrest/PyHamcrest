from hamcrest.core.base_matcher import Matcher
from hamcrest.core.core.isequal import equal_to


def wrap_shortcut(x):
    if isinstance(x, Matcher):
        return x
    else:
        return equal_to(x)
