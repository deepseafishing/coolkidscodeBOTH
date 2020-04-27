def isValid(self, s: str) -> bool:
  open = {}
  close = {}
  for a in [['(', ')'], ['{', '}'], ['[', ']']]:
    open[a[0]] = a[1]
    close[a[1]] = a[0]
  print(open, close)
  stack = []
  for c in s:
    if (c in open):
      stack.append(c)
    elif (c in close):
      if(len(stack) == 0 or stack.pop() != close[c]):
        return False
    else:
      return False

  return len(stack) == 0
