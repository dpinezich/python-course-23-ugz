def sum(a, b):
  if not isinstance(a, float):
    raise TypeError("Error: a is not a number")

  if not isinstance(b, float):
    raise TypeError("Error: b is not a number")

  return a + b
