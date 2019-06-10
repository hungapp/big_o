# snakes and ladders

# (u):
# q = [u]
# visted[u] = true
# dist[u] = 0

# while q.qsize() > 0:
#   u = q.pop()
#   if u == 100:
#       return dist[u]
#   for i in range(1, 7):
#     if u + i > 100: break
#     v = ways[u + i]
#     if !visited[v]:
#       visited[v] = true
#       dist[v] = dist[u] + 1
#       q.push(v)


# Read no. testcase
# For each in testcase:
#   Init ways = [i for i in range(101)] 
#   Read n
#   For i in range(n):
#     u, v => ways[u] = v
#   ...
#   print(find (i))


  