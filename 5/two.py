import string as s
from one import react_polymer

polymer = list(open('in.txt').read())
res = len(polymer)

for lower, upper in zip(s.ascii_lowercase, s.ascii_uppercase):
    chopped = [unit for unit in polymer if unit not in (lower, upper)]
    reaction = react_polymer(chopped)
    res = min(res, reaction)

print(res)