from collections import deque
t = {"matt1": ["dan_lee", "123"],
     "dan_lee": ["jason", "anne"],
     "123": ["john"],
     "jason": [],
     "anne": [],
     "john": []
     }


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        distance = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, 1), (-1, -1), (1, -1)]
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                r, c = queue.popleft()
                grid[r][c] = 2
                if (r, c) == (m-1, n-1):
                    return distance
                for d in directions:
                    nr, nc = d[0]+r, d[1]+c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            distance += 1
        return -1


'''
[[0,0,0],
[1,1,0],
[1,1,0]]

# 0 1 0
# 0 1
# 0 1
# 0 0 1 0
# 0 0

[[0, 1],
 [1, 0]]
ans -> 1
answer -> 3



	 1
   /
  2   |
	\
	  3
'''


def get_neighbors(i, j, graph, row_limit, col_limit):
    neibors = []
    for r in range(max(0, i - 1), min(row_limit, i + 1)):
        for c in range(max(0, j - 1), min(col_limit, j + 1)):
            if (i != r or j != c):
                neibors.append((r, c))

    print(neibors)
    return neibors


def shortest_path(graph):
    row_limit = len(graph) - 1
    col_limit = len(graph[0]) - 1
    if graph[row_limit][col_limit] != 0:
        return False

    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])
    distance = 0
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()

        for n_r, n_c in get_neighbors(cur_r, cur_c, graph, row_limit, col_limit):
            if (n_r, n_c) not in visited:
                if (n_r, n_c) == (row_limit, col_limit):
                    return cur_d + 1
                queue.append((n_r, n_c, cur_d + 1))
                visited.add((n_r, n_c))

    return False


tt = [[0, 0, 0],
      [1, 1, 0],
      [1, 1, 0]]
print(shortest_path(tt))


# count_reports("anne") -> 1
# count_reports(dan_lee) -> 3

# def count_reports2(person, graph):
#   if person not in graph:
#     return 0
#   total = 1
#   if not graph[person]:
#     return 1
#   for subordinate in graph[person]:
#     total += count_reports2(subordinate, graph)
#   return total

# # print(count_reports2("matt1", t))
# def count_reports(person, graph):
#   def dfs(person):
#     if not graph[person]:
#       return 1
#     total = 1

#     for boss in graph[person]:
#       total += dfs(boss)

#     return total

#   return dfs(person)


# print(count_reports('anne', t))
# print(count_reports('dan_lee', t))
# print(count_reports('matt1', t))
