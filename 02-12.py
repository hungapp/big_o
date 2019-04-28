
# 602B - Constant Range
n = int(input())
a = list(map(int, input().split()))

fre = [0] * (100001)
unique = 0
j = 0
max_length = 0

for i in range(n):
    if fre[a[i]] == 0:
        unique += 1
    fre[a[i]] += 1

    while j < n and unique == 3:
        fre[a[j]] -= 1
        if fre[a[j]] == 0:
            unique -= 1
        j += 1

    max_length = max(max_length, i - j + 1)

print(max_length)

# 6C
n = int(input())
t = list(map(int, input().split()))

a = b = 0
ta = tb = 0
i = 0
j = n - 1

while i <= j:
    if ta <= tb:
        ta += t[i]
        i += 1
    else:
        tb += t[j]
        j -= 1

print(i, n - i)

# 381A - Card Game
n = int(input())
c = list(map(int, input().split()))

score = [0, 0]
player = 0
i = 0
j = n - 1

while i <= j:
    if c[i] > c[j]:
        score[player] += c[i]
        i += 1
    else:
        score[player] += c[j]
        j -= 1
    player = 1 - player

print(score[0], score[1])
