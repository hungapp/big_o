# audiophobia
import queue
INF = int(1e9)


class Node():
    def __init__(self, id, d):
        self.id = id
        self.d = d

    def __lt__(self, other):
        return self.d <= other.d


def prims(src):
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
    dist = [-1] * (c+1)

    stack.append(startId)
    visited[startId] = True

    while len(stack) > 0 and not visited[stopId]:
        u = stack.pop()
        for edge in mst_graph[u]:
            if visited[edge.id] == False:
                visited[edge.id] = True
                stack.append(edge.id)
                dist[edge.id] = max(dist[u], edge.d)

    return 'no path' if dist[stopId] == -1 else dist[stopId]


case = 0
blank_line = False
while True:
    case += 1
    c, s, q = map(int, input().split())
    if c == s == q == 0:
        break

    if blank_line:
        print()

    graph = [[] for i in range(c + 1)]
    mst_graph = [[] for i in range(c + 1)]
    path = [-1 for i in range(c + 1)]
    visited = [False for _ in range(c + 1)]
    decibels = [INF for _ in range(c + 1)]

    for i in range(s):
        c1, c2, d = map(int, input().split())
        graph[c1].append(Node(c2, d))
        graph[c2].append(Node(c1, d))

    for i in range(1, c + 1):
        if not visited[i]:
            prims(i)

    print('Case #{}'.format(case))
    for i in range(q):
        c1, c2 = map(int, input().split())
        print(dfs(c1, c2))

    blank_line = True

# 1 2 3 4 5 6
# a b c d e f
# 5 6 8 4 5 7

# 2->6 : 2->1->3->6

# blackout

INF = int(1e9)


class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def prims(src, graph, mst=False):
    visited = [False for _ in range(n + 1)]
    costs = [INF for _ in range(n + 1)]
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    costs[src] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            c = neighbor.cost
            if not visited[v] and c < costs[v]:
                costs[v] = c
                pq.put(Node(v, c))
                if mst:
                    path[v] = Node(u, c)
    min_cost = sum(costs[2:])
    return min_cost


t = int(input())
for c in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append(Node(b, c))
        graph[b].append(Node(a, c))
    first_min = prims(1, graph, True)

    second_min = INF
    res = []
    for u in range(1, n + 1):
        if path[u] == -1:
            continue
        else:
            # graph_temp = graph

            v = path[u].id
            c = path[u].cost
            # print(v, c)

            for i in range(len(graph[u])):
                if graph[u][i].id == v and graph[u][i].cost == c:
                    graph[u][i].cost = INF
            for i in range(len(graph[v])):
                if graph[v][i].id == u and graph[v][i].cost == c:
                    graph[v][i].cost = INF

            x = prims(1, graph)
            # print(x)
            second_min = min(second_min, x)

            for i in range(len(graph[u])):
                if graph[u][i].id == v and graph[u][i].cost == INF:
                    graph[u][i].cost = c
            for i in range(len(graph[v])):
                if graph[v][i].id == u and graph[v][i].cost == INF:
                    graph[v][i].cost = c
    print(first_min, second_min)
