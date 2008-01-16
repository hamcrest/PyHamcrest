from hamcrest.core.selfdescribing import SelfDescribing


class SelfDescribingValue(SelfDescribing):

    def __init__(self, value):
        self.value = value

    def describe_to(self, description):
        description.append_value(self.value)
