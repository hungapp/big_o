# Arbitrage

INF = 1e9


def FloydWarshall(graph, arbitrage):
    for i in range(n):
        for j in range(n):
            arbitrage[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arbitrage[i][j] < arbitrage[i][k] * arbitrage[k][j]:
                    arbitrage[i][j] = arbitrage[i][k] * arbitrage[k][j]


tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [[INF for i in range(n)] for j in range(n)]
    arbitrage = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        graph[i][i] = 1

    c = []
    for i in range(n):
        c.append(input())

    m = int(input())
    for i in range(m):
        ci, r, cj = input().split()
        ci = c.index(ci)
        cj = c.index(cj)
        graph[ci][cj] = float(r)

    FloydWarshall(graph, arbitrage)
    result = 'No'
    for i in range(n):
        if arbitrage[i][i] > graph[i][i]:
            result = 'Yes'
    print('Case {}: {}'.format(tc, result))
    tc += 1
    input()


# Max Comp
INF = 1e9


def FloydWarshall(graph):
    for k in range(49):
        for i in range(49):
            for j in range(49):
                if i <= k <= j and graph[i][j] < graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


t = int(input())
for tc in range(t):
    n = int(input())
    graph = [[0 for i in range(49)] for j in range(49)]  # range(49)

    for i in range(n):
        s, e, c = map(int, input().split())
        if c > graph[s][e]:
            graph[s][e] = c
    FloydWarshall(graph)
    print(graph[0][48])  # result = graph[0][48]

# City of Hope

INF = 1e9


def FloydWarshall(graph):
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


def fill_graph(graph, direction, s, e, c):
    s = ord(s.lower()) - 97  # ord(s) - ord('A')
    e = ord(e.lower()) - 97
    if direction == 'U':
        graph[s][e] = min(c, graph[s][e])
    else:
        graph[s][e] = min(c, graph[s][e])
        graph[e][s] = min(c, graph[e][s])


while True:
    n = int(input())
    if n == 0:
        break
    y_graph = [[INF for i in range(26)] for j in range(26)]
    m_graph = [[INF for i in range(26)] for j in range(26)]
    for i in range(26):
        y_graph[i][i] = 0
        m_graph[i][i] = 0
    for i in range(n):
        r, d, s, e, c = input().split()
        c = int(c)
        if r == 'Y':
            fill_graph(y_graph, d, s, e, c)
        else:
            fill_graph(m_graph, d, s, e, c)
    FloydWarshall(y_graph)
    FloydWarshall(m_graph)

    s1, s2 = map(lambda x: ord(x) - ord('A'), input().split())
    min_dist = INF
    res = []

    for i in range(26):
        if y_graph[s1][i] != INF and m_graph[s2][i] != INF:
            if y_graph[s1][i] + m_graph[s2][i] < min_dist:
                min_dist = y_graph[s1][i] + m_graph[s2][i]
                res = [i]
            elif y_graph[s1][i] + m_graph[s2][i] == min_dist:
                res.append(i)
    if min_dist == INF:
        print('You will never meet.')
    else:
        print(min_dist, end='')
        for i in range(len(res)):
            print(' ' + chr(res[i] + ord('A')), end='')
        print()
