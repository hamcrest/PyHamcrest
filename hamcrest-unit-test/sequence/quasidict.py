class QuasiDictionary:
    def iteritems(self):
        return QuasiDictionaryItemIterator()
        
    def iterkeys(self):
        return QuasiDictionaryKeyIterator()
        
    def itervalues(self):
        return QuasiDictionaryValueIterator()


class BaseQuasiDictionaryIterator:
    def __init__(self):
        self.index = 1
    
    def __iter__(self):
        return self

    def next(self):
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
