# 224B - Arrays
n, k = map(int, input().split())
a = list(map(int, input().split()))

fre = [0] * 1000000
unique, j = 0, 0

for i in range(n):
    fre[a[i]] += 1

    if fre[a[i]] == 1:
        unique += 1

    while unique == k:
        fre[a[j]] -= 1

        if fre[a[j]] == 0:
            print(j + 1, i + 1)
            exit()

        j += 1
print('-1 -1')

# 279B - Books
n, t = map(int, input().split())
a = list(map(int, input().split()))

read_time, j, max_book = 0, 0, 0

for i in range(n):
    read_time += a[i]
    while read_time > t:
        read_time -= a[j]
        j += 1
    max_book = max(max_book, i - j + 1)

print(max_book)

# 161A - dress em in vests
n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
c = []
d = []

while i < n and j < m:
    if b[j] >= a[i] - x and b[j] <= a[i] + y:
        c.append(i + 1)
        d.append(j + 1)
        i += 1
        j += 1
    elif a[i] + y < b[j]:
        i += 1
    else:
        j += 1

print(len(c))
for i in range(len(c)):
    print(c[i], d[i])

# 430B - Balls Game
n, k, x = map(int, input().split())
c = list(map(int, input().split()))
insert_pos = []
balls = []

i = 0
while i < n:
    j = 1
    while i + j < n and c[i + j] == c[i]:
        j += 1

    if c[i] == x and j == 2:
        insert_pos.append(len(balls))

    balls.append((c[i], j))
    i = i + j

max_balls = 0
for pos in insert_pos:
    count_balls = 2
    i = pos - 1
    j = pos + 1

    while i >= 0 and j < len(balls):
        if balls[i][0] == balls[j][0] and balls[i][1] + balls[j][1] >= 3:
            count_balls += balls[i][1] + balls[j][1]
            i -= 1
            j += 1
        else:
            break

    max_balls = max(max_balls, count_balls)


print(max_balls)


# 387B - George and Round
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0

while i < n and j < m:
    if b[j] >= a[i]:
        j += 1
        i += 1
    else:
        j += 1

print(n - i)


n = int(input())
l = list(map(int, input().split()))


alive = [1] * 1000000

j = 0
for i in range(1, n):
    if l[i] != 0:
        j = max(i - l[i], j)
        while j < i:
            alive[j] = 0
            j += 1

life = 0
for i in range(n):
    if alive[i] == 1:
        life += 1

print(life)
