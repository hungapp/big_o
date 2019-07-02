def DFS(s):
  stack = []
  stack.append(s)
  visited[s] = True
  while len(stack) > 0:
    u = stack.pop()
    for v in graph[u]:
      if visited[v] == True:
        return 'SIM'

      if visited[v] == False:
        visited[v] = True
        stack.append(v)
  return 'NAO'


def DFS(s):
  visited[s] = True
  inPath[s] = True

  for u in graph[s]:
    if inPath[u] == True:
      return True
    else:
      if DFS(u):
        return True

  inPath[s] = False
  return False

    1
   /  ^
  2 -> 4


t = int(input())
for _ in range (t):
  n, m = map(int, input().split())
  graph = [[] for _ in range (n+1)]
  docs = [False for _ in range (n+1)]
  visited = [False for _ in range (n+1)]
  for i in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    docs[a] = docs[b] = True

  for i in range (1, n + 1):
    if docs[i] and not visited[i]:
      print(DFS(i))


# def DFS(s):
#   stack = []
#   stack.append(s)
#   visited[s] = True
#   while len(stack) > 0: 
#     u = stack.pop()
#     for v in graph[u]:
#       if visited[v] == True:
#         return 'SIM'
        
#       if visited[v] == False:
#         visited[v] = True
#         stack.append(v)
#   return 'NAO'

# def DFS(s):
#   visited[s] = True
#   inPath[s] = True

#   for u in graph[s]:
#     if inPath[u] == True:
#       return True
#     else:
#       if DFS(u):
#         return True

#   inPath[s] = False
#   return False

#     1
#    /  ^
#   2 -> 4


# t = int(input())
# for _ in range (t):
#   n, m = map(int, input().split())
#   graph = [[] for _ in range (n+1)]
#   docs = [False for _ in range (n+1)]
#   visited = [False for _ in range (n+1)]
#   for i in range (m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     docs[a] = docs[b] = True

#   for i in range (1, n + 1):
#     if docs[i] and not visited[i]:
#       print(DFS(i))


letter = list("ALLIZZWELL")
found = False

def dfs(sx, sy, step):
  visited[sx][sy] = True
  if step == len(letter):
    found = True
    return

  for i in range(4):
    x = ux + dx[i]
    y = uy + dy[i]

    if x in range(R) and y in range(C) and not visited[x][y] and graph[x][y] == letter[step]:
      dfs(x, y, step + 1)
  
  visited[sx][sy] = False



for i in range(R):
  for j in range(C):
    if not visited[i][j] and graph[i][j] == letter[0]:
      dfs(i, j, 1)
      if found == True:
        break

print('YES' if found else 'NO')









