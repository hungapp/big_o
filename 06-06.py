# build road
import queue
INF = int(1e9)

class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def Dijkstra(s):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.id
    w = top.dist
    for neighbor in graph[u]:
      if w + neighbor.dist < dist[neighbor.id]:
        dist[neighbor.id] = w + neighbor.dist
        pq.put(Node(neighbor.id, dist[neighbor.id]))
      

n = int(input())
graph = [[] for i in range(501)]
dist = [INF for i in range(501)]
for i in range(n):
  a, b, w = map(int, input().split())
  graph[a].append(Node(b, w))
  graph[b].append(Node(a, w))
u = int(input())
Dijkstra(u)
q = int(input())
for i in range(q):
  v = int(input())
  if dist[v] == INF:
    print('NO PATH')
  else: 
    print(dist[v]) 
