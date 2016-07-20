from pyaccum import accumulate

# ORIGINAL CODE

class A:
    def foo(self, x):
        return list(self._foo(x))
    
    def _foo(self, x):
        ys = []
        for i in range(len(x)):
            if pred1(x):
                ys.append(x.bar(i))
            elif pred2(x):
                ys.append(x)
            else:
                ys.append(None)
        return B(ys)

# NEW CODE

class A:
    @accumulate(lambda ys: list(B(ys)))
    def foo(self, x):
        for i in range(len(x)):
            if pred1(x):
                yield x.bar(i)
            elif pred2(x):
                yield x
            else:
                yield None
