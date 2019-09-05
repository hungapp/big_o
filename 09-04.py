class Node:
    def __init__(self):
        self.child = dict()
        self.weight = 0


def addWord(root, s, w):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.weight < w:
            temp.weight = w


def findMaxWeight(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.weight


root = Node()
n, q = map(int, input().split())
for i in range(n):
    line = list(input().split())
    addWord(root, line[0], int(line[1]))
for i in range(q):
    query = input()
    print(findMaxWeight(root, query))
