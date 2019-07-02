INF = 1e9

class Line:
  def __init__(self, u, v, w):
    self.u = u
    self.v = v
    self.w = w

def BellmanFord(s):
  global graph, weight, n, m
  weight[s] = 0
  for i in range(n - 1):
    for line in graph:
      u, v, w = line.u, line.v, line.w
      if weight[u] != INF and weight[u] + w < weight[v]:
        weight[v] = weight[u] + w
  for line in graph:
    u, v, w = line.u, line.v, line.w
    if weight[u] + w < weight[v]:
      weight[v] = -INF


while True:
  n, m, q, s = map(int, input().split())
  if n == 0:
    break
  graph = []
  weight = [INF] * (n + 1)
  for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append(Line(u, v, w))
  BellmanFord(s)
  for k in range(q):
    f = int(input())
    if weight[f] == INF:
      print('Impossible')
    elif weight[f] == -INF :
      print('-Infinity')
    else:
      print(weight[f])
  print()

# MPI Maelstrom
import queue
INF = 1e9

class Node:
  def __init__(self, j, x):
    self.j = int(j)
    self.x = int(x)
  def __lt__(self, other):
    return self.x < other.x

def Dijkstra():
  global graph, time
  pq = queue.PriorityQueue()
  pq.put(Node(0, 0))
  while pq.empty() == False:
    top = pq.get()
    u = top.j
    w = top.x
    for neighbor in graph[u]:
      if w + neighbor.x < time[neighbor.j]:
        time[neighbor.j] = w + neighbor.x
        pq.put(Node(neighbor.j, time[neighbor.j]))


n = int(input())
graph = [[] for _ in range(n + 1)]
time = [INF] * n
for i in range(1, n):
  a = input().split()
  for j in range(i):
    if a[j] != 'x':
      graph[i].append(Node(j, a[j]))
      graph[j].append(Node(i, a[j]))
Dijkstra()
min_time = -INF
for i in range(n):
  min_time = max(time[i], min_time)
print(min_time)

# for i in range(n - 1):    # for i in range(1, n):
#   #a = list(map(int, input().split()))   # Error for 'x'
#   a = input().split()
#   for j in range(i + 1):  #   for j in range(i):
#     if a[j] != 'x':
#       graph.append((i + 1, j + 1, int(a[j])))
#       graph.append((j + 1, i + 1, int(a[j])))

# BellmanFord(0)

# max_dist = -INF
# for i in range(n):
#   max_dist = max(dist[i], max_dist)  
