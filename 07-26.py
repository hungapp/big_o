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