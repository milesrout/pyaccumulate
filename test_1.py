from pyaccum import accumulate

# ORIGINAL CODE

class Conjunction:
    def min_spec(self, neginst, attributes):
        return list(self._min_spec(neginst, attributes))
    
    def _min_spec(self, neginst, attributes):
        for i in range(len(self)):
            if is_wildcard(self[i]):
                for v in attributes[i]:
                    hypothesis = Conjunction(v if i == j else self[j] for j in range(len(self)))
                    if not hypothesis.match(neginst):
                        yield hypothesis
                    
# NEW CODE

class Conjunction:
    @accumulate(list)
    def min_spec(self, neginst, attributes):
        for i in range(len(self)):
            if is_wildcard(self[i]):
                for v in attributes[i]:
                    hypothesis = Conjunction(v if i == j else self[j] for j in range(len(self)))
                    if not hypothesis.match(neginst):
                        yield hypothesis