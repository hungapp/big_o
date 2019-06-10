# that is your queue

import queue

case = 0
while True:
    p, c = map(int, input().split())
    if p == c == 0:
        break
    case += 1
    print('Case ', case, ':', sep='')
    population = queue.Queue()
    # because p < 1000000, c < 1000 while the program won't run more that c cases so should only populate upto the min of the two)
    for i in range(1, min(c + 1, p + 1)):
        population.put(i)

    for _ in range(c):
        command = input().split()
        if command[0] == 'N':
            print(population.queue[0])
            population.put(population.get())
        else:
            population.put(int(command[1]))
            for i in range(population.qsize()):
                if population.queue[0] == int(command[1]):
                    population.get()
                else:
                    population.put(population.get())
