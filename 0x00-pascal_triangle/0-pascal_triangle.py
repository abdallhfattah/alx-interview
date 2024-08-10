def pascal_triangle(n):
  init = []
  if n <= 0: return []
  else:
    while n > 0:
      if len(init) > 0:
        to_append = [1]
        for i in range(len(init[-1]) - 1):
          to_append.append(init[-1][i] + init[-1][i+1])
        to_append.append(1)
        init.append(to_append)
          
      else:
        init.append([1])
      n -= 1
  return init
