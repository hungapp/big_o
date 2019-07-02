# extended traffic

INF = 1e9

class Triad:
  def __init__(self, source, target, point):
    self.source = source
    self.target = target
    self.point = point

def BellmanFord():
  global graph, point, n, m
  point[1] = 0
  for i in range(2, n):
    for j in range(m):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].point
      if point[u] + w < point[v]:
        point[v] = point[u] + w

t = int(input())
for c in range(t):
  print('Case {}:'.format(c + 1))
  input()
  n = int(input())
  graph = []
  point = [INF for _ in range(n + 1)]
  busyness = [0] + list(map(int, input().split()))
  m = int(input())
  for i in range(m):
    u, v = map(int, input().split())
    w = (busyness[v] - busyness[u]) ** 3
    graph.append(Triad(u, v, w))
  BellmanFord()
  q = int(input())
  for _ in range(q):
    d = int(input())
    print(point[d] if point[d] != INF and point[d] >= 3 else "?")


  INF = 1e9

INF = 1e9

class Trader:
  def __init__(self, i, j, c):
    self.i = i
    self.j = j
    self.c = -c

def BellmanFord():
  global profit, market, n, m
  profit[1] = 0
  for i in range(2, n + 1):       # Loop n - 1:
    for j in range(m):             # for edge in market:
      u = market[j].i
      v = market[j].j
      w = market[j].c
      if profit[u] != INF and profit[u] + w < profit[v]:
        profit[v] = profit[u] + w
  for i in range(m):
    u = market[i].i
    v = market[i].j
    w = market[i].c
    if profit[u] != INF and profit[u] + w < profit[v]:
      return True
  return False      

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  market = []
  profit = [INF for _ in range(n + 1)]
  for k in range(m):
    i, j, c = map(int, input().split())
    market.append(Trader(i, j, c))
  res = BellmanFord()
  print('Yes' if res == True else 'No')


# blue brothers
class Street:
  def __init__(self, a, b, p):
    self.a = a
    self.b = b
    self.p = p / 100

def BellmanFord():
  global graph, percent, n, m
  percent[1] = 1
  for i in range (1, n):
    for street in graph:
      u, v, w = street.a, street.b, street.p
      if percent[u] * w > percent[v]:
        percent[v] = percent[u] * w
  

while True:
  line = list(map(int, input().split()))
  if len(line) == 1:
    break

  n, m = line[0], line[1]
  graph = []
  percent = [0 for _ in range(n + 1)]
  for i in range(m):
    a, b, p = map(int, input().split())
    graph.append(Street(a, b, p))
    graph.append(Street(b, a, p))
  BellmanFord()
  print('{:.6f} percent'.format(percent[n] * 100))