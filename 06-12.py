import queue
INF = int(1e9)

class Node:
  def __init__(self, id, len):
    self.id = id
    self.len = len
  def __lt__(self, other):
    return self.len <= other.len

def Dijkstra(s, length, graph):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  length[s] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.id
    w = top.len
    for neighbor in graph[u]:
      if w + neighbor.len < length[neighbor.id]:
        length[neighbor.id] = w + neighbor.len
        pq.put(Node(neighbor.id, length[neighbor.id]))


no_ds = int(input())
for _ in range(no_ds):
  n, m, k, s, t = map(int, input().split())
  graphS = [[] for _ in range(n + 1)]
  graphT = [[] for _ in range(n + 1)]
  for i in range(m):
    d, c, l = map(int, input().split())
    graphS[d].append(Node(c, l))
    graphT[c].append(Node(d, l))
  lengthS = [INF for _ in range(n + 1)]
  lengthT = [INF for _ in range(n + 1)]
  Dijkstra(s, lengthS, graphS)
  Dijkstra(t, lengthT, graphT)

  # u, v, d
  # u -> v
  # u <- v tuong duong

  # lengthS[u] + d + lengthT[v]

  min_length = INF  
  for j in range(k):
    u, v, q = map(int, input().split())
    min_length = min(min_length, lengthS[u] + q + lengthT[v],  lengthT[u] + q + lengthS[v])

  if min_length < INF:
    print(min_length)
  else:
    print(-1)
  