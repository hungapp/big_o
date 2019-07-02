import queue

n, b = map(int, input().split())
q = queue.Queue()
processing = 0


for _ in range(n):
    t, d = map(int, input().split())

    while q.qsize() != 0 and t >= q.queue[0]:
        q.get()

    if q.qsize() <= b:
        processing = max(t, processing) + d
        q.put(processing)
        print(processing)
    else:
        print(-1)

# mass molecule


def atom_mass(c): return 1 if c == 'H' else 12 if c == 'C' else 16


s = input()
molecule = []

for l in s:
    if l == '(':
        molecule.append(l)
    if l.isalpha():
        molecule.append(atom_mass(l))
    if l == ')':
        big_atom = 0
        while molecule[-1] != '(':
            big_atom += molecule.pop()
        molecule.pop()
        molecule.append(big_atom)
    if l.isdigit():
        molecule.append(molecule.pop() * int(l))

print(sum(molecule))
