def react_polymer(polymer):
    stack = []
    for unit in polymer:
        if abs(ord(stack[-1] if stack else ' ') - ord(unit)) == 32:
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)

res = react_polymer(list(open('in.txt').read()))
print(res)