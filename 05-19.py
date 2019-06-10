# night at the museum

wheel = input()
pointer = 'a'
count = 0

for c in wheel:
    dist = abs(ord(pointer) - ord(c))
    
    if dist < 13:
        count = count + dist
    else:
        count = count + (26 - dist)
    
    pointer = c

print(count)

#  Vitaly and Strings

s = list(input())
t = list(input())

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        s[i] = 'a'
    else:
        s[i] = chr(ord(s[i]) + 1)
        break


print(''.join(s) if s != t else "No such string")