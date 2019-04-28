def DFS(s):
    stack = []
    visited[s] = True
    distance[s] = 0
    stack.append(s)
    while len(stack) > 0:
        u = stack[-1]
        stack.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)
                distance[v] = distance[u] + 1


N = int(input())
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
distance = [-1 for i in range(N + 1)]
countries = []
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
Q = int(input())
for i in range(Q):
    x = int(input())
    countries.append(x)

DFS(1)


id = countries[0]
min_distance = distance[id]

for x in countries:
    if distance[x] < min_distance | | (distance[x] == min_distance and x < id):
        id = x
        min_distance = distance[x]

# min_distance = distance[countries[0]]
# for x in countries:
#   min_distance = min(min_distance, distance[x])


# id = max(countries)
# for x in countries:
#   if distance[x] == min_distance and x < id:
#     id = x

print(id)
