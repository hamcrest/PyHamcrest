class GeneratorForm(object):
    def _sequence(self, *objects):
        for i in objects:
            yield i


class SequenceForm(object):
    def _sequence(self, *objects):
        return list(objects)


class CollectionForm(object):
    def _sequence(self, *objects):
        return {obj: 0 for obj in objects}
