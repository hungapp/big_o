import bisect

c = 1
while True:
    n, q = map(int, input().split())
    if n == q == 0:
        break
    marbles = []
    for i in range(n):
        marbles.append(int(input()))
    marbles.sort()
    print('CASE# {}:'.format(c))
    for i in range(q):
        query = int(input())
        pos = bisect.bisect_left(marbles, query, 0, n)
        if not pos == n and marbles[pos] == query:
            print('{} found at {}'.format(query, pos + 1))
        else:
            print('{} not found'.format(query))
    c += 1


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
c = 0
for i in range(n):
    x = numbers[i] + k
    pos = bisect.bisect_left(numbers, x, i + 1, n)
    if not pos == n and numbers[pos] == x:
        c += 1
print(c)


# eko


def totalWood(trees, height):
    wood = 0
    i = 0
    while trees[i] >= height:
        wood += trees[i] - height
        i += 1
        if i == n:
            break
    return wood


n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
left = 0
right = trees[0]
max_height = 0
while left <= right:
    mid = (left + right) // 2
    if totalWood(trees, mid) >= m:
        max_height = mid
        left = mid + 1
    else:
        right = mid - 1
print(max_height)


