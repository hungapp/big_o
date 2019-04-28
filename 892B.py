# 892B - Wrath C1
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


# C2

n = int(input())
l = list(map(int, input().split()))

life = 1
for i in range(1, n):
    if l[i] == 0:
        life += 1
    elif l[i] != 0 and l[i - 1] == 0:
        life_to_kill = l[i] - 1
        j = 1
        while life_to_kill > 0 and l[i - j] == 0:
            life -= 1
            life_to_kill -= 1
            j += 1

print(life)

# correct
n = int(input())
a = list(map(int, input().split()))
j = n - 1
count = 0

for i in range(n - 1, -1, -1):
    j = min(i, j)
    last_pos_kill = max(0, i - a[i])

    if j > last_pos_kill:
        count += (j - last_pos_kill)
        j = last_pos_kill

print(n - count)
