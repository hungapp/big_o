# key merger

import queue


def BFS(s):
    global lock, used, keys, times
    q = queue.Queue()
    q.put(s)
    used[s] = True
    times[s] = 0
    flag = True
    while not q.empty() and flag:
        u = q.get()

        for key in keys:
            v = (u * key) % 100000

            if used[v] == False:  # visited is the value of merged keys, not just single keys
                used[v] = True
                q.put(v)
                times[v] = times[u] + 1
            if v == lock:
                flag = False
                break

    return times[lock]


hero_key, lock = map(int, input().split())
n = int(input())
keys = list(map(int, input().split()))

times = [-1 for _ in range(100001)]
used = [False for _ in range(100001)]
print(BFS(hero_key))


# 2 conditions
# 1 2 o thuoc bien
# 2 2 o noi vs nhau


# 2 conditions
# 1 2 o thuoc bien
# 2 2 o noi vs nhau

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(sx, sy):
    global gate, visited, M, m, n
    fx = gate[1][0]
    fy = gate[1][1]
    q = queue.Queue()
    visited[sx][sy] = True
    q.put((sx, sy))

    while not q.empty():
        ux, uy = q.get()
        if ux == fx and uy == fy:
            break

        for i in range(4):
            vx = ux + dx[i]
            vy = uy + dy[i]

            if vx in range(m) and vy in range(n) and not visited[vx][vy] and M[vx][vy] == '.':
                visited[vx][vy] = True
                q.put((vx, vy))

    return visited[fx][fy]


t = int(input())
for _ in range(t):
    M = []
    m, n = map(int, input().split())
    for i in range(m):
        row = input()
        M.append(row)

    visited = [[False for _ in range(n)] for i in range(m)]

    # 1st cond
    gate = []  # chay ngang
    for i in range(n):
        if M[0][i] == '.':
            gate.append((0, i))
        if M[m-1][i] == '.' and m - 1 != 0:
            gate.append((m - 1, i))

    for j in range(1, m - 1):
        if M[j][0] == '.':
            gate.append((j, 0))
        if M[j][n-1] == '.' and n - 1 != 0:
            gate.append((j, n - 1))

    if len(gate) != 2:
        print('invalid')
    else:
        # 2nd cond
        if (BFS(gate[0][0], gate[0][1])):
            print('valid')
        else:
            print('invalid')
