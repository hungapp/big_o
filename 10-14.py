parent = []
ranks = []


def makeSet(n):
    global parent, ranks, count
    parent = [i for i in range(n + 1)]
    ranks = [0 for i in range(n + 1)]
    count = [1 for i in range(n + 1)]


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        count[up] = count[up] + count[vp]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        count[vp] = count[up] + count[vp]
    else:
        parent[up] = vp
        count[vp] = count[up] + count[vp]
        ranks[vp] += 1


no_test = int(input())
for _ in range(no_test):
    n, m = map(int, input().split())
    makeSet(n)
    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
    print(max(count))

# lost
parent = []
ranks = []


def makeSet(n):
    global parent, ranks, count
    parent = [i for i in range(n + 1)]
    ranks = [0 for i in range(n + 1)]
    count = [1 for i in range(n + 1)]


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        count[up] = count[up] + count[vp]
        count[vp] = 0
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        count[vp] = count[up] + count[vp]
        count[up] = 0
    else:
        parent[up] = vp
        count[vp] = count[up] + count[vp]
        count[up] = 0
        ranks[vp] += 1


n, q = map(int, input().split())
makeSet(n)
for i in range(q):
    u, v = map(int, input().split())
    unionSet(u, v)
    largest = -1
    smallest = 2 ** 32
    for v in range(1, n + 1):
        if v == parent[v]:
            largest = max(largest, count[v])
            smallest = min(smallest, count[v])
    print(largest - smallest)
