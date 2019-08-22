import bisect

n = int(input())
temp = list(map(int, input().split()))
prices = []
min_loss = 1e9

prices.append(temp[0])
for i in range(1, n):
    prices.append(temp[i])
    prices.sort()
    pos = bisect.bisect_right(prices, temp[i])
    if pos > 0 and pos < len(prices) - 1:
        price_to_buy = prices[pos]
        loss = price_to_buy - temp[i]
        min_loss = min(min_loss, loss)

print(min_loss)


def upperbound(root, x):
    if root == None:
        return None
    if root.key <= x:
        return upperbound(root.right, x)
    else:  # root.key > x
        tmp = upperbound(root.left, x)
        if tmp == None:
            return root.key
        else:
            return tmp


# dictionary
class Scanner:
  def __gen__():
    while True:
      for x in input().strip().split():
        yield x
  
  gener = __gen__()

  def next():
    return Scanner.gener.__next__()

Sc = Scanner

def normalized(s):
  res = ''
  for x in s:
    if x.isalpha():
      res += x.lower()
    else:
      res += ' '
  return res


words = set()
while True:
  try:
    for word in normalized(Sc.next()).split():
      words.add(word)
    
  except EOFError:
    print(*sorted(words), sep='\n')
    break




