"""Library of Matcher implementations."""

from hamcrest.core import *
from collection import *
from integration import *
from number import *
from object import *
from text import *

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

__all__ = [
    'has_entry',
    'has_entries',
    'has_key',
    'has_value',
    'is_in',
    'has_item',
    'has_items',
    'contains_inanyorder',
    'contains',
    'only_contains',
    'match_equality',
    'close_to',
    'greater_than',
    'greater_than_or_equal_to',
    'less_than',
    'less_than_or_equal_to',
    'has_length',
    'has_property',
    'has_string',
    'equal_to_ignoring_case',
    'equal_to_ignoring_whitespace',
    'contains_string',
    'ends_with',
    'starts_with',
]
