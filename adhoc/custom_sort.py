def customSort(arr):
  map = {}
  for idx, val in enumerate(arr):
    if val in map:
      map[val] = (map[val][0] + 1, map[val][1], val)
    else:
      map[val] = (1, idx, val)

  ret = list(map.values())
  ret.sort(key=lambda x: (-x[0], x[1]))

  r = []

  # r = [x[2] for x in ret for x in range(x[0])]
  for x in ret:
    for _ in range(x[0]):
      r.append(x[2])

  return r

print(customSort([3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]))
print(customSort([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]))
# [8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999]`
# input: [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
# output: [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]
