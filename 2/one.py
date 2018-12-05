from collections import Counter

two = three = 0
for line in open('in.txt'):
    counts = Counter(line).values()
    two += 2 in counts
    three += 3 in counts

print(two * three)