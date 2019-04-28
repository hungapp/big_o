# 169A
n, a, b = map(int, input().split())
h = list(map(int, input().split()))

temp = sorted(h)
print(temp[-a] - temp[b - 1])

# sorted reverse then print(temp[a - 1] - temp[a])

# 149A
k = int(input())
a = list(map(int, input().split()))

temp = sorted(a, reverse=True)
height = i = 0
while height < k and i < len(a):
    height += temp[i]
    i += 1

if height < k:
    print(-1)
else:
    print(i)

# 439B
n, x = map(int, input().split())
c = list(map(int, input().split()))

temp = sorted(c)
time = 0


for i in range(n):
    time += temp[i] * x
    if x > 1:
        x -= 1

print(time)

# 551A
n = int(input())
a = list(map(int, input().split()))

temp = sorted(a, reverse=True)
rating = [0] * (2001)

for i in range(n):
    if rating[temp[i]] == 0:
        rating[temp[i]] = i + 1

for score in a:
    print(rating[score], end=' ')

"""
for i in range (n):
  for j in range (n):
    if a[i] == temp[j]:
      a[i] = j + 1
      break

print(*a, sep=' ')"""
