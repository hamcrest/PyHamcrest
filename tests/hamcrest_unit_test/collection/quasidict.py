from collections.abc import Iterator

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class QuasiDictionary(object):
    def items(self):
        return QuasiDictionaryItemIterator()

    def keys(self):
        return QuasiDictionaryKeyIterator()

    def values(self):
        return QuasiDictionaryValueIterator()


class BaseQuasiDictionaryIterator(Iterator):
    def __init__(self):
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 3:
            raise StopIteration
        result = self.indexToResult()
        self.index += 1
        return result


class QuasiDictionaryItemIterator(BaseQuasiDictionaryIterator):
    def indexToResult(self):
        return (self.index, str(self.index))


class QuasiDictionaryKeyIterator(BaseQuasiDictionaryIterator):
    def indexToResult(self):
        return self.index


class QuasiDictionaryValueIterator(BaseQuasiDictionaryIterator):
    def indexToResult(self):
        return str(self.index)
