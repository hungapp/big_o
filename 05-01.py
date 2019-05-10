# monk
import heapq

n = int(input())
a = list(map(int, input().split()))

# h = []
# for i in range (n):
#   heapq.heappush(h, a[i])
#   if i < 2:
#     print(-1)
#   else:
#     pop1 = heapq.heappop(h)
#     pop2 = heapq.heappop(h)
#     pop3 = heapq.heappop(h)
#     print(pop1 * pop2 * pop3 * (-1))
#     heapq.heappush(h, pop1)
#     heapq.heappush(h, pop2)
#     heapq.heappush(h, pop3)

h = []  # Min (three largest elements)
for i in range(n):
    if i < 2:
        print(-1)
        heapq.heappush(h, a[i])
    else:
        if i == 2:
            heapq.heappush(h, a[i])
        elif a[i] > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, a[i])
        pop1 = heapq.heappop(h)
        pop2 = heapq.heappop(h)
        pop3 = heapq.heappop(h)
        print(pop1 * pop2 * pop3)
        heapq.heappush(h, pop1)
        heapq.heappush(h, pop2)
        heapq.heappush(h, pop3)

    if i < 3:
        heappush
    else:
        if ...

    if i < 2:
        print(-1)
    else:
        pop
        push

# trending topic
import heapq

class Topic :
  def __init__(self, id, z, cR):
    self.id = id
    self.z = z
    self.currentZ = cR
    self.changeZ = self.currentZ - self.z
 
  def getIDandZ(self):
    return(self.id, self.currentZ)
 
  def __lt__(self, other):
    return (self.changeZ > other.changeZ) or (self.changeZ == other.changeZ and self.id > other.id) 
  
h = []
n = int(input())
for i in range (n):
  l = list(map(int, input().split()))
  currentZ = 50 * l[2] + 5 * l[3] + 10 * l[4] + 20 * l[5]
  t = Topic(l[0], l[1], currentZ)
  heapq.heappush(h, t)
  
for i in range (5):
  trendyTopic = heapq.heappop(h)
  print(*trendyTopic.getIDandZ())

# add all
import heapq

while True:
  n = int(input())
  if n == 0:
    break
  a = list(map(int, input().split()))
  h = []
  sum = 0
  heapq.heapify(a)
  while len(a) > 1:
    pop1 = heapq.heappop(a)
    pop2 = heapq.heappop(a)
    temp = pop1 + pop2
    heapq.heappush(a, temp)
    sum = sum + temp
  print(sum)




