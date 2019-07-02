# wormholes
INF = 1e9

class Triad():
  def __init__(self, source, target, time):
    self.source = source
    self.target = target
    self.time = time

def BellmanFord():
  global dist, graph, n, m
  dist[0] = 0
  for i in range(1, n):
    for j in range(m):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].time
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
  for i in range(m):
    u = graph[i].source
    v = graph[i].target
    w = graph[i].time
    if dist[u] + w < dist[v]:
      return False
  return True

c = int(input())
for _ in range(c):
  n, m = map(int, input().split())
  graph = []
  dist = [INF for _ in range(n + 1)]
  for i in range(m):
    x, y, t = map(int, input().split())
    graph.append(Triad(x, y, t))
  res = BellmanFord()
  if res == False: # Dau = bi sai
    print('possible')
  else:
    print('not possible')
