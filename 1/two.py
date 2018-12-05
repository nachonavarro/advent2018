from itertools import cycle

seen, freq = set(), 0
for change in cycle(open('in.txt')):
    freq += int(change)
    if freq in seen:
        break
    seen.add(freq)

print(freq)