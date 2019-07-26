# Social Network
INF = 1e9


def FloydWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]
                dist[i][j] = dist[i][k] + dist[k][j]


t = int(input())
for c in range(t):
    line = list(input())
    n = len(line)
    graph = []
    dist = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        if i != 0:
            line = list(input())
        graph.append(line)

        for j in range(n):
            if line[j] == 'N' and i != j:
                graph[i][j] = INF
            elif line[j] == 'N' and i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = 1

    FloydWarshall(graph, dist)

    max_friends = 0
    id_max = 0

    for i in range(n):
        friend_no = 0
        for j in range(n):
            if dist[i][j] == 2:
                friend_no += 1
        if friend_no > max_friends:
            id_max = i
            max_friends = friend_no
    print(id_max, max_friends)
