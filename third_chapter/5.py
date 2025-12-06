def apply_twice(func, value):
  intermediate = func(value)
  result = func(intermediate)
      
  return result
