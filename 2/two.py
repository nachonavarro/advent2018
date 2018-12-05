from itertools import combinations

for box1, box2 in combinations(open('in.txt'), 2):
    similar = ''.join(letter1 for letter1, letter2 in zip(box1, box2) if letter1 == letter2)
    if len(similar) == len(box1) - 1:
        break
print(similar)