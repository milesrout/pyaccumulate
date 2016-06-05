from pyaccum import accumulate

# ORIGINAL CODE

class Conjunction:
    def min_gen(self, inst):
        return [self._min_gen(inst)]
    
    def _min_gen(self, inst):
        features = []
        for i in range(len(self)):
            if self[i] is None:
                features.append(inst[i])
            elif is_wildcard(self[i]) or self[i] == inst[i]:
                features.append(self[i])
            else:
                features.append(Wildcard)
        return Conjunction(tuple(features))

# NEW CODE

class Conjunction:
    @accumulate(lambda x: [Conjunction(tuple(x))])
    def min_gen(self, inst):
        for i in range(len(self)):
            if self[i] is None:
                yield inst[i]
            elif is_wildcard(self[i]) or self[i] == inst[i]:
                yield self[i]
            else:
                yield Wildcard