# pyaccumulate

I think we can all agree that generators are nice to write in Python, much nicer than explicitly collecting into a data structure (like a list, a set or a dictionary). But sometimes you want those strict semantics, and sometimes you want to manipulate the return values of a function in one place. So you can either do it manually:

```python3
def foo(a, b, c):
  result = []
  for x in a:
    if pred(x):
      result.append(baz(x))
      return result
    ...
    ...
    result.append(bar(x))
  return result
```

or write a generator and a wrapper function for that generator:

```python3

@functools.wraps(foo_impl)
def foo(*args, **kwds):
  return list(foo_impl(*args, **kwds))
  
def foo_impl(a, b, c):
  for x in a:
    if pred(x):
      return (yield baz(x))
    ...
    ...
    yield bar(x)
```

I don't find that very aesthetically pleasing. So I wrote this:

```
@accumulate(list)
def foo(a, b, c):
  for x in a:
    if pred(x):
      return (yield baz(x))
    ...
    ...
    yield bar(x)
```

Easy.
