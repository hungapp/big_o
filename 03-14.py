
# Compilers and Parsers_COMPILER_CodeChef


def getPrefixLength(exp):
    temp = []
    count = 0
    for e in exp:
        if e == "<":
            temp.append(e)
        else:
            if len(temp) == 0:
                break
            else:
                temp.pop()
                count += 2

    if len(temp) != 0:
        count = 0
    return count


t = int(input())
for _ in range(t):
    exp = input()
    print(getPrefixLength(exp))


# Transform the Expression_ONP_SPOJ
n = int(input())
for _ in range(n):
    operator = []
    var = []
    expr = input()

    for c in expr:
        if c.isalpha():
            var.append(c)
        elif c != ')':
            operator.append(c)
        else:
            while operator:
                op = operator.pop()
                if op == '(':
                    break
                var.append(op)

    print(*var, sep='')
