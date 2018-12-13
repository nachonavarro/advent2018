def play(times):
    plants = [i for i, pot in enumerate(state) if pot == "#"]
    for _ in range(times):    
        first, last = plants[0] - 4, plants[-1] + 5
        pots = ''.join('#' if pot in plants else '.' for pot in range(first, last))
        plants = [first + i + 2 for i in range(last - first - 4) if rules[pots[i:i + 5]] == '#']
    return sum(plants)

lines = open('in.txt').read().splitlines()
state = lines[0][15:]
rules = {line[:5]: line[9] for line in lines[2:]}
res = play(20)
print(res)