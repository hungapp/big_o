INF = 1e9


def FloydWarshall(graph):
    for k in range(21):
        for i in range(21):
            for j in range(21):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


tc = 1
while True:
    try:
        graph = [[INF for i in range(21)] for j in range(21)]
        for i in range(1, 20):
            line = list(map(int, input().split()))
            x = line[0]
            for j in range(1, x + 1):
                graph[i][line[j]] = graph[line[j]][i] = 1
        FloydWarshall(graph)
        n = int(input())

        print('Test Set #{}'.format(tc))
        for i in range(n):
            s, f = map(int, input().split())import math


INF = 1e9

# Thunder Mountain


class Scanner:
  def __gen__():
    while True:
      buff = input().strip().split()
      for x in buff:
        yield x
  __sc__ = __gen__()

  def next():
    return Scanner.__sc__.__next__()


def FloydWarshall(graph):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][j] > graph[i][k] + graph[k][j]:
          graph[i][j] = graph[i][k] + graph[k][j]


N = int(Scanner.next())
for c in range(1, N + 1):
  n = int(Scanner.next())
  graph = [[INF for i in range(n)] for j in range(n)]
  xs = []
  ys = []
  for i in range(n):
    x, y = int(Scanner.next()), int(Scanner.next())
    xs.append(x)
    ys.append(y)
  for i in range(n):
    for j in range(n):
      if i == j:
        graph[i][j] = 0
      else:
        dist = math.sqrt((xs[i] - xs[j])**2 + (ys[i] - ys[j])**2)
        if dist > 10:
          graph[i][j] = INF
        else:
          graph[i][j] = dist
  FloydWarshall(graph)

  print('Case #{}:'.format(c))
  max_dist = 0
  break_flag = False

  for i in range(n):
    if break_flag:
      break

    for j in range(n):
      if graph[i][j] == INF:
        break_flag = True
        break
      elif graph[i][j] > max_dist:
        max_dist = graph[i][j]

  if break_flag:
    print('Send Kurdy')
  else:
    print('{:.4f}'.format(max_dist))
  print()

            print('{:2d} to {:2d}: {}'.format(s, f, graph[s][f]))
        tc += 1
        print()
    except EOFError:
        break

