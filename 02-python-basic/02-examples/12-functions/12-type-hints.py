def sum(a: float, b: float) -> float:
  if not (isinstance(a, float) and isinstance(b, float)):
    raise TypeError("Error: a or b is not a number")

  return a + b
