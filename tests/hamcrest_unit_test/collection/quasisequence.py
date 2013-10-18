__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class QuasiSequence:
    def __iter__(self):
        return QuasiSequenceIterator()

    def __len__(self):
        return 2


class QuasiSequenceIterator:
    def __init__(self):
        self.index = 1

    def __iter__(self):
        return self

    def next(self):
        if self.index >= 3:
            raise StopIteration
        result = self.index
        self.index += 1
        return result
