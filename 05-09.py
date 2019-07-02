import queue

#class PQ(MyObject)... - Primary datatype

#user-defined datatype
class PQ:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value

while True:
  try:
    n = int(input())
  except EOFError:
    break

  s = []
  q = queue.Queue()
  pq = queue.PriorityQueue()
  qf = True
  sf = True
  pqf = True

  for i in range (n):
    t, x = map(int, input().split())
    
    if t == 1:
      s.append(x)
      q.put(x)
      pq.put(PQ(x))  
    else:
      if len(s):
        if x != s.pop():
          sf = False
        if x != q.get():
          qf = False
        if x != pq.get().value:
          pqf = False
      else:
        sf = qf = pqf = False

  s = qf + pqf + sf
  if s == 0:
    print('impossible')
  elif s >= 2:
    print('not sure')
  elif (sf == True):
    print('stack')
  elif (qf == True):
    print('queue')
  elif (pqf == True):
    print('priority queue')


import queue

q = int(input())
pq = queue.PriorityQueue()
pqRemove = queue.PriorityQueue()

for i in range(q):
    line = input()

    if line[0] == '1':
        value = int(line.split()[1])
        pq.put(value)
    elif line[0] == '2':
        value = int(line.split()[1])
        pqRemove.put(value)
    else:
        while not pqRemove.empty() and pq.queue[0] == pqRemove.queue[0]:
            pq.get()
            pqRemove.get()

        print(pq.queue[0])
