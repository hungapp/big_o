import bisect

n = int(input())
ladies = list(map(int, input().split()))
q = int(input())
heights = list(map(int, input().split()))

for i in range(q):
    luchu_height = heights[i]
    tall_pos = bisect.bisect_right(ladies, luchu_height)
    short_pos = tall_pos - 1
    while short_pos > -1 and ladies[short_pos] >= luchu_height:
        short_pos -= 1

    if short_pos < 0:
        a = 'X'
    else:
        a = ladies[short_pos]
    if tall_pos >= n:
        b = 'X'
    else:
        b = ladies[tall_pos]
    print(a, b)

# monkey and oiled bamboo
def success(k):
  i = 0
  while (i < n):
    if rungs[i + 1] - rungs[i] == k:
      k -= 1
    elif rungs[i + 1] - rungs[i] > k:
      return False
    i += 1
  return True

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  rungs = [0] + list(map(int, input().split()))
  left = 0
  right = rungs[n - 1]
  res = 0
  while left <= right:
    mid = (left + right) // 2
    if success(mid):
      right = mid - 1
      res = mid
    else:
      left = mid + 1
  print('Case {}: {}'.format(t, res))
