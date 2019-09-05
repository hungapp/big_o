n = int(input())
penguines = dict()
for i in range(n):
  kind = input()
  if kind not in penguines:
    penguines[kind] = 1
  else:
    penguines[kind] += 1
result = max(penguines, key = penguines.get)
print(result)

# megacity
n, s = map(int, input().split())
population = s
rs = dict()
success = False
for i in range(n):
  x, y, k = map(int, input().split())
  r = x**2 + y**2
  if r in rs:
    rs[r] += k
  else:
    rs[r] = k

for key in sorted(rs.keys()):
  population += rs[key]
  
  if population >= 1000000:
    print('{:.7f}'.format(key ** 0.5))
    success = True
    break

if not success:
  print(-1)

# han solo
n, x0, y0 = map(int, input().split())
lines = set()
x_line = 0
for i in range(n):
  x, y = map(int, input().split())
  if x == x0:
    x_line = 1
  else:
    a = (y - y0) / (x - x0)
    b = y0 - a * x0
    lines.add((a, b))

print(len(lines) + x_line)

# network
import queue

def BFS():
  global network, visited, dist
  q = queue.Queue()
  visited['Isenbaev'] = True
  q.put('Isenbaev')
  while not q.empty():
    u = q.get()
    for v in network[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)
        dist[v] = dist[u] + 1


n = int(input())
network = {}
visited = {}
dist = {}
for i in range(n):
  line  = list(input().split(' '))
  for elem in line:
    if elem not in network:
      network[elem] = set()
      visited[elem] = False
      dist[elem] = 0
      
    for elem_add in line:
      if elem_add != elem:
        network[elem].add(elem_add)

if 'Isenbaev' in network:
  BFS()
  
for key, value in sorted(dist.items()):
  if not visited[key]:
    print(key, 'undefined')
  else:
    print(key, value)
  
