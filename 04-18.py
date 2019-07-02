# berland lake 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def on_border(x, y):
    ##result = True
    return x == 0 or x == n - 1 or y == 0 or y == m - 1
    ##  result = False
    # return result


def DFS(sx, sy):
    global n, m, b_map, visited, lakes
    stack = []
    visited[sx][sy] = True
    stack.append((sx, sy))
    is_ocean = False

    water_area = []

    while len(stack) > 0:
        ux, uy = stack.pop()
        water_area.append((ux, uy))
        if on_border(ux, uy):
            is_ocean = True

        for i in range(4):
            vx = ux + dx[i]
            vy = uy + dy[i]
            if vx in range(n) and vy in range(m) and not visited[vx][vy] and b_map[vx][vy] == '.':
                visited[vx][vy] = True
                stack.append((vx, vy))

    if is_ocean == False:
        lakes.append(water_area)


n, m, k = map(int, input().split())
b_map = []
for i in range(n):
    line = input()
    b_map.append(list(line))

visited = [[False for _ in range(m)] for _ in range(n)]
lakes = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and b_map[i][j] == '.':
            DFS(i, j)

lakes = sorted(lakes, key=lambda x: len(x))
count = 0
for i in range(len(lakes) - k):
    count += len(lakes[i])
    for j in range(len(lakes[i])):
        x, y = lakes[i][j]
        b_map[x][y] = '*'

print(count)
for line in range(n):
    print(*b_map[line], sep='')
