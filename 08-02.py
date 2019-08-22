def calSumTransfer(m):
    global a
    sum_transfer = 0
    for i in range(n):
        sum_transfer += max(a[i] - m, 0)
    return sum_transfer


n, k = map(int, input().split())
a = list(map(int, input().split()))
left = min(a)
right = max(a)
sum_energy = sum(a)

mid = left

while right - left > 10 ** -6:
    mid = (left + right) / 2
    sum_lost = calSumTransfer(mid) * k / 100

    if mid * n < sum_energy - sum_lost:
        left = mid
    else:
        right = mid

print('%.9f' % mid)
