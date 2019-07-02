import heapq


class MaxHeap(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)


n = int(input())
a = list(map(int, input().split()))
h = []
for i in range(n):
    heapq.heappush(h, MaxHeap(a[i]))
    if len(h) < 3:
        print(-1)
    else:
        pop1 = heappop()
        pop2 = heappop()
        pop3 = heappop()
        print(pop1 * pop2 * pop3)
        heappush(pop1)
        heappush(pop2)
        heappush(pop3)

for i in range(n):
    heap.push()
    if < 3:
        print(-1)
    else:

        max = []
        product = 1
        for _ in range(3):
            product *= heapq.heappop(h).value
        print(product)
