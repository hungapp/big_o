class Scanner:
  import sys
  def __init__(self, istream = sys.stdin):
    self.tokenizer = Scanner.__tokenizer__(istream)
  def __tokenizer__(istream):
    for line in istream:
      for token in line.strip().split():
        yield token
    while True:
      yield None
  def next(self, type = str, rep = 1):
    if rep == 1:
      return type(self.tokenizer.__next__())
    return [type(self.tokenizer.__next__()) for i in range(rep)]

def DFS(s):
  global n, graph
  visited = [False for _ in range (n + 1)]
  stack = []
  visited[s] = True
  stack.append(s)
  explode = 1
  while len(stack) > 0:
    u = stack.pop()
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        explode += 1
        stack.append(v)
  return explode

sc = Scanner()
n, m = sc.next(int, 2)
graph = [[] for _ in range (n + 1)]
for i in range (m):
  u, v = sc.next(int, 2)
  graph[u].append(v)

exploded_bombs = 0
for i in range (1, n + 1):
  exploded_bombs = max(exploded_bombs, DFS(i))

print(exploded_bombs)