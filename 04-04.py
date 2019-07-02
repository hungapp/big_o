# slick

import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(sx, sy):
    q = queue.Queue()
    visited[sx][sy] = True
    q.put((sx, sy))
    slick_size = 1

    while not q.empty():
        ux, uy = q.get()
        for i in range(4):
            vx = ux + dx[i]
            vy = uy + dy[i]

            if vx in range(n) and vy in range(m) and not visited[vx][vy] and M[vx][vy] == 1:
                visited[vx][vy] = True
                q.put((vx, vy))
                slick_size += 1
    return slick_size


while True:
    M = []
    n, m = map(int, input().split())
    if n == m == 0:
        break

    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        M.append(row)

    slicks = [0] * (250 * 250 + 1)
    slick_no = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and M[i][j] == 1:
                slicks[BFS(i, j)] += 1
                slick_no += 1

    print(slick_no)
    for i in range(len(slicks)):
        if slicks[i] != 0:
            print(i, slicks[i])

# use list instead of queue
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

MAX = 251
table = [None] * MAX
slick = [0] * (MAX * MAX)
q = [None] * (MAX * MAX)


def BFS(sr, sc):
    left = right = 0
    q[0] = (sr, sc)
    table[sr][sc] = '0'
    count = 1

    while left <= right:
        ur, uc = q[left]
        left += 1

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(N) and c in range(M) and table[r][c] == '1':
                right += 1
                q[right] = (r, c)
                table[r][c] = '0'
                count += 1

    slick[count] += 1


while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    for i in range(N):
        table[i] = input().split()
        for j in range(M):
            slick[i * M + j + 1] = 0

    nslicks = 0

    for i in range(N):
        for j in range(M):
            if table[i][j] == '1':
                nslicks += 1
                BFS(i, j)

    print(nslicks)

    for i in range(1, N * M + 1):
        if slick[i]:
            print(i, slick[i], sep=' ')
