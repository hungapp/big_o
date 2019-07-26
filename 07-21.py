# asterix and obelix

INF = 1e9


def FloydWarshall():
    for k in range(1, c + 1):
        for i in range(1, c + 1):
            for j in range(1, c + 1):
                if graph[i][j] + feast[i][j] > graph[i][k] + graph[k][j] + max(feast[i][k], feast[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    feast[i][j] = max(feast[i][k], feast[k][j])


tc = 1
blank_line = False

while True:
    c, r, q = map(int, input().split())
    if c == r == q == 0:
        break
    graph = [[INF for i in range(c + 1)] for j in range(c + 1)]
    feast = [[0 for i in range(c + 1)] for j in range(c + 1)]
    feast_cost = list(map(int, input().split()))

    for i in range(1, c + 1):
        graph[i][i] = 0
        feast[i][i] = feast_cost[i - 1]

    for i in range(1, c + 1):
        for j in range(1, c + 1):
            feast[i][j] = max(feast_cost[i - 1], feast_cost[j - 1])

    for i in range(r):
        c1, c2, d = map(int, input().split())
        graph[c1][c2] = d
        graph[c2][c1] = d

    FloydWarshall()
    FloydWarshall()

    if blank_line:
        print()
    blank_line = True

    print('Case #{}'.format(tc))
    for i in range(q):
        c1, c2 = map(int, input().split())
        print(graph[c1][c2] + feast[c1][c2] if graph[c1][c2] < INF else -1)
    tc += 1

    
INF = 1e9
def FloydWarshall(graph, k):
  for i in range(n):
    for j in range(n):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

n = int(input())
graph = []
for i in range(n):
  line = list(map(int, input().split()))
  graph.append(line)
delete_vertices = list(map(int, input().split()))

res = []
for k in range(n - 1, -1, -1):
  v = delete_vertices[k] - 1
  FloydWarshall(graph, v)
  part_sum = 0
  for i in range(k, n):
    for j in range(k, n):
      u, v = delete_vertices[i] - 1, delete_vertices[j] - 1
      part_sum += graph[u][v]
  res.append(part_sum)

print(*res[::-1])