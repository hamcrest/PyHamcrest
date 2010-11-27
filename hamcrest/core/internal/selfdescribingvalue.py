__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from hamcrest.core.selfdescribing import SelfDescribing


class SelfDescribingValue(SelfDescribing):

    def __init__(self, value):
        self.value = value

    def describe_to(self, description):
        description.append_value(self.value)
