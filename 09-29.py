# Simulate network
import queue
INF = int(1e9)

class Node():
  def __init__(self, id, latency):
    self.id = id
    self.latency = latency
  def __lt__(self, other):
    return self.latency <= other.latency

def prims(src):
  pq = queue.PriorityQueue()
  pq.put(Node(src, 0))
  latency[src] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      l = neighbor.latency
      if not visited[v] and l < latency[v] :
        latency[v] = l
        pq.put(Node(v, l))


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
latency = [INF for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
  a, b, l = map(int, input().split())
  graph[a].append(Node(b, l))
  graph[b].append(Node(a, l))
prims(1)
latency = latency[1:]

try:
  q = int(input())
  c = list(map(int, input().split()))
except EOFError:
  c = []
  pass

c.sort()
latency.sort(reverse=True)
i = 0
while(i < len(latency) and i < len(c)):
  if latency[i] < c[i]:
    i += 1
  else:
    latency[i] = c[i]
    i += 1
print(sum(latency))



# Audiophibia
import queue
INF = int(1e9)

class Node():
  def __init__(self, id, d):
    self.id = id
    self.d = d
  def __lt__(self, other):
    return self.d <= other.d

def prims(src):
  path = [-1 for i in range(c + 1)]
  visited = [False for _ in range(c + 1)]
  decibels = [INF for _ in range(c + 1)]
  pq = queue.PriorityQueue()
  
  pq.put(Node(src, 0))
  decibels[src] = 0
  
  while not pq.empty():
    top = pq.get()
    u = top.id
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      d = neighbor.d
      if not visited[v] and d < decibels[v]:
        decibels[v] = d
        pq.put(Node(v, d))
        path[v] = u
        
  for v in range(1, c + 1):
    u = path[v]
    d = decibels[v]
    if u == -1:
      continue
    mst_graph[v].append(Node(u, d))
    mst_graph[u].append(Node(v, d))
  
def dfs(startId, stopId):
  visited = [False for _ in range(c+1)]
  stack = []
  dist = [0] * (c+1)
  
  stack.append(startId)
  visited[startId] = True
  
  while len(stack) > 0 and not visited[stopId]:
    u = stack.pop()
    for edge in mst_graph[u]:
      if visited[edge.id] == False:
        visited[edge.id] = True
        stack.append(edge.id)
        dist[edge.id] = max(dist[u], edge.d)
  
  return 'no path' if dist[stopId] == 0 else dist[stopId]
          
    
case = 0
while True:
  case += 1
  c, s, q = map(int, input().split())
  if c == s == q == 0:
    break
  graph = [[] for i in range(c + 1)]
  mst_graph = [[] for i in range(c + 1)]

  for i in range(s):
    c1, c2, d = map(int, input().split())
    graph[c1].append(Node(c2, d))
    graph[c2].append(Node(c1, d))
 
  print('Case #{}'.format(case))
  for i in range(q):
    c1, c2 = map(int, input().split())
    prims(c1)
    print(dfs(c1, c2))
   
  print()
  
# 1 2 3 4 5 6
# a b c d e f
# 5 6 8 4 5 7

# 2->6 : 2->1->3->6

