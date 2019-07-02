# 677A
# input n, h
n, h = map(int, input().split())

# input list
a = list(map(int, input().split()))

fence_length = 0
for i in range(n):
    if a[i] <= h:
        fence_length += 1
    else:
        fence_length += 2

print(fence_length)


# 673A
# input n
n = int(input())

# input list
a = list(map(int, input().split()))
# a.insert(0,0)

t = 0

for i in range(n):
    if t + 15 < a[i]:
        print(t + 15)
        exit()
    else:
        t = a[i]

print(min(90, t + 15))
