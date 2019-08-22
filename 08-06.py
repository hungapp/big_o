from sys import stdin
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = set(map(int, input().split()))
    if len(a) > x:
        print('Average')
    elif len(a) < x:
        print('Bad')
    else:
        print('Good')


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    students = set()
    for j in range(n):
        students.add(temp[j])
    for j in range(n, len(temp)):
        if temp[j] in students:
            print('YES')
        else:
            print('NO')
        students.add(temp[j])


line = list(map(int, stdin.read().split()))
n = line[0]
years = set()

for i in range(1, n + 1):
    years.add(line[i])

m = line[n + 1]
c = 0
for i in range(m):
    if line[n + 2 + i] in years:
        c += 1
print(c)
