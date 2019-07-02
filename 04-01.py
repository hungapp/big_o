# guilty prince in the desert
import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(sx, sy):
    global visited, M, w, h
    q = queue.Queue()
    visited[sx][sy] = True
    q.put((sx, sy))
    no_cell = 1

    while not q.empty():
        ux, uy = q.get()
        for i in range(4):
            vx = ux + dx[i]
            vy = uy + dy[i]

            if vx in range(h) and vy in range(w) and not visited[vx][vy] and M[vx][vy] == '.':
                visited[vx][vy] = True
                q.put((vx, vy))
                no_cell += 1

    return no_cell


t = int(input())

# O(T * W * H)
for c in range(t):
    M = []
    w, h = map(int, input().split())

    for i in range(h):
        row = input()
        for j in range(w):
            if row[j] == '@':
                sx = i
                sy = j
        M.append(row)

    visited = [[False for _ in range(w)] for _ in range(h)]
    #print('Case ', c + 1, ': ', BFS(sx, sy), sep = '')
    print('Case {}: {}'.format(c + 1, BFS(sx, sy)))
