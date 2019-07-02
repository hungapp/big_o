# 557B
n, w = map(int, input().split())
a = list(map(int, input().split()))

temp = sorted(a)

m = min(temp[0], temp[n] / 2)
total = 3 * n * m

print(min(total, w))

# 334B
points = []
x = []
y = []
for _ in range(8):
    a, b = map(int, input().split())
    points.append((a, b))
    x.append(a)
    y.append(b)

    # points.append(list(map(int, input().split)))
x.sort()
y.sort()
x_uk = y_uk = 1
x_mid = y_mid = 0
for i in range(7):
    if x[i + 1] != x[i]:
        x_uk += 1
        if x_uk == 2:
            x_mid = x[i + 1]

    if y[i + 1] != y[i]:
        y_uk += 1
        if y_uk == 2:
            y_mid = y[i + 1]

    if x_uk > 3 or y_uk > 3:
        print('ugly')
        exit()

for i in range(8):
    if points[i][0] == x_mid and points[i] == y_mid:
        print('ugly')
        exit()

print('respectable')


# key
unique_x = []
unique_y = []
fre_x = [False] * (10 ** 6 + 5)
fre_y = [False] * (10 ** 6 + 5)
points = []

for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

    if not fre_x[x]:
        fre_x[x] = True
        unique_x.append(x)

    if not fre_y[y]:
        fre_y[y] = True
        unique_y.append(y)

if len(fre_x) != 3 or len(fre_y) != 3:
    print('ugly')
    exit()

unique_x.sort()
unique_y.sort()
points.sort()
index = 0

for i in range(3):
    for j in range(3):
        if i == j == 1:
            continue
        if unique_x[i] == points[index][0] and unique_y[j] == points[index][1]:
            index += 1
        else:
            print('ugly')

print('respectable')
