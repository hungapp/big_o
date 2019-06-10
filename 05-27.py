import heapq

q = int(input())

h = []
delete = []
for _ in range (q):
  line = list(map(int, input().split()))
  if len(line) == 2:
    if line[0] == 1:
      heapq.heappush(h, line[1])
    else: 
      heapq.heappush(delete, line[1]) 
  else:
    while len(delete) > 0 and h[0] == delete[0]:
      heapq.heappop(h)
      heapq.heappop(delete)
    print(h[0])


  