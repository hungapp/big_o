# Breadth First Search: Shortest Reach

import queue


def BFS(s):

    dist[s] = 0
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                q.put(v)
                # path[v] = u
                dist[v] = dist[u] + 1


def distanceOf(s, f):
    global path, distance
    if s == f:
        return
    if path[f] == -1:
        distance = -1
        return
    else:
        distance += 6
        distanceOf(s, path[f])


def printDistance(s):
    global distance
    distances = []

    for i in range(1, n + 1):
        if i == s:
            continue
        distances.append(dist[i] * 6 if visited[i] else -1)
        # N * O(N) = O(N^2)
        # if i == s:
        #   continue
        # distance = 0
        # distanceOf(s, i)
        # distances.append(distance)
    print(*distances, sep=' ')


q_no = int(input())
distance = 0

for _ in range(q_no):
    n, m = map(int, input().split())
    MAX = n + 1
    path = [-1 for i in range(MAX)]  # isn't neccessary, dist is enough
    graph = [[] for i in range(MAX)]
    visited = [False for i in range(MAX)]

    dist = [-1 for i in range(MAX)]  # list comprehension

    # O(M)

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = int(input())
    BFS(s)
    # O(N + M)
    printDistance(s)
    # O(N^2)

    # O(Q * max(N ^ 2, N + M))


key, lock = map(int, input().split())
n = int(input())
keys = map(int, input().split())

q = queue.Queue()
used = [False for _ in range(n + 1)]
merged_keys = [-1 for _ in range(n + 1)]
