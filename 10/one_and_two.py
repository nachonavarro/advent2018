import re

info = [[int(x) for x in re.findall(r'-?\d+', line)] for line in open('in.txt')]

upper_bound = 30000
smallest = upper_bound
for diff in range(upper_bound):
    min_x = min_y = upper_bound
    max_y = max_x = 0
    for x, y, dx, dy in info:
        diff_x, diff_y = x + diff * dx, y + diff * dy
        min_x, min_y = min(min_x, diff_x), min(min_y, diff_y)
        max_x, max_y = max(max_x, diff_x), max(max_y, diff_y)
        boundary = max_x - min_x + max_y - min_y
    if boundary < smallest:
        smallest = boundary
        smallest_diff = diff
        coords = max_x, min_x, max_y, min_y

max_x, min_x, max_y, min_y = coords
width, height = max_x - min_x + 1, max_y - min_y + 1
view = [['.' for _ in range(width)] for _ in range(height)]
for x, y, dx, dy in info:
    view[y + smallest_diff * dy - min_y][x + smallest_diff * dx - min_x] = '#'

for line in view:
    print(''.join(line))

print(smallest_diff)