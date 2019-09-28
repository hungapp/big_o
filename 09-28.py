import queue
INF = int(1e9)


class Node:
    def __init__(self, id, weight):
        self.weight = weight
        self.id = id

    def __lt__(self, other):
        return self.weight <= other.weight


def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    weight[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.weight
            if not visited[v] and w < weight[v]:
                weight[v] = w
                pq.put(Node(v, w))


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
weight = [INF for i in range(n + 1)]
visited = [False for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
prims(1)
totalWeight = 0
for i in range(1, n + 1):
    totalWeight += weight[i]
print(totalWeight)
