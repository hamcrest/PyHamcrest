# coding: utf-8
import six
import pytest
from mock import sentinel, patch

from hamcrest.core.base_description import BaseDescription
from hamcrest.core.selfdescribing import SelfDescribing

__author__ = "Chris Rose"
__copyright__ = "Copyright 2015 hamcrest.org"
__license__ = "BSD, see License.txt"


class Collector(BaseDescription):
    def __init__(self):
        self.appended = []

    def append(self, obj):
        self.appended.append(obj)

class Described(SelfDescribing):
    def describe_to(self, desc):
        desc.append('described')


@pytest.fixture
def desc():
    return Collector()

def test_append_text_delegates(desc):
    desc.append_text(sentinel.Text)
    assert desc.appended == [sentinel.Text]


@pytest.mark.parametrize('described, appended', (
    (Described(), 'described'),
    pytest.mark.skipif(six.PY3, reason="py2 only")((six.u('unicode-py2'), "'unicode-py2'")),
    pytest.mark.skipif(six.PY3, reason="py2 only")((six.b('bytes-py2'), "'bytes-py2'")),
    pytest.mark.skipif(six.PY2, reason="py3 only")((six.u('unicode-py3'), "'unicode-py3'")),
    pytest.mark.skipif(six.PY2, reason="py3 only")((six.b('bytes-py3'), "<b'bytes-py3'>")),
    (six.u("\U0001F4A9"), six.u("'{0}'").format(six.u("\U0001F4A9"))),
))
def test_append_description_types(desc, described, appended):
    desc.append_description_of(described)
    assert ''.join(desc.appended) == appended


@pytest.mark.parametrize("char, rep", (
    ("'", r"'"),
    ("\n", r"\n"),
    ("\r", r"\r"),
    ("\t", r"\t"),
))
def test_string_in_python_syntax(desc, char, rep):
    desc.append_string_in_python_syntax(char)
    assert ''.join(desc.appended) == "'{0}'".format(rep)
