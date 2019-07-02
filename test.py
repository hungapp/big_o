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
