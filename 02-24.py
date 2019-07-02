n = int(input())
l = list(map(int, input().split()))

# c1

fre = [0] * 1001

unique = 0
for i in range(n):
    if fre[temp[i]] == 0:
        unique += 1
    fre[temp[i]] += 1

print(max(fre), unique)
# -> O(max(n, 1001))
# c2
temp = sorted(l)
n_uniques = 1
count = 1
longest_count = 1

for i in range(1, n):
    if temp[i] != temp[i - 1]:
        n_uniques += 1
        count = 1
    else:
        count += 1
        longest_count = max(longest_count, count)

print(n_uniques, longest_count)
# -> O(nlogn)

# 481B
n = int(input())
a = list(map(int, input().split()))

temp = sorted(a)
pos = []

for i in range(n):
    if a[i] != temp[i]:
        pos.append(i)
if not pos:
    print('yes')
    print(1, 1)
    exit()

a[pos[0]:pos[len(pos)-1] + 1] = reversed(a[pos[0]:pos[len(pos)-1] + 1])


for i in range(n):
    if a[i] != temp[i]:
        print('no')
        exit()

print('yes')
print(pos[0] + 1, pos[len(pos)-1] + 1)
