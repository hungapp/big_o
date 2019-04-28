# 10935 uva throwing cards
import queue

while True:
  n = int(input())
  if n == 0:
    break
    
  deck = queue.Queue()
  for i in range (1, n + 1):
    deck.put(i)

  discarded = []
  # size >= 2:
  # discarded.add(deck.get())
  # deck.add(deck.get())

  while deck.qsize() >= 2:
    discarded.append(deck.get())
    deck.put(deck.get())

  print("Discarded cards: ", end='')
  print(*discarded, sep=', ')
  print("Remaining card:", deck.get())


#   street parade
while True:
  n = int(input())
  if n == 0:
    break

  t = list(map(int, input().split()))
  side = []
  order = 1
  i = 0
  
  while i < n:
    if side and side[-1] == order:
      order += 1
      side.pop()
    elif t[i] == order:
      i += 1
      order += 1
    else:
      side.append(t[i])
      i += 1

  while side and side[-1] == order:
    side.pop()
    order += 1

  if order == n + 1:
    print('yes')
  else:
    print('no')