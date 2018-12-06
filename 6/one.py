from collections import Counter

manhattan = lambda xy, uv: abs(xy[0] - uv[0]) + abs(xy[1] - uv[1])
flatten = lambda ls: [item for sub in ls for item in sub]
coords = [tuple(int(x) for x in pair.split(',')) for pair in open('in.txt')]
width, height = max(x for x, y in coords) + 1, max(y for x, y in coords) + 1
view = [[None] * width for _ in range(height)]
edge_points = set()

def closest_coord_to(point):
    closest  = min(coords, key=lambda coord: manhattan(coord, point))
    shortest = manhattan(closest, point)
    return closest if sum(1 for coord in coords if manhattan(point, coord) == shortest) == 1 else None

for x in range(width):
    for y in range(height):
        view[y][x] = closest_coord_to((x, y))
        if x in (0, width - 1) or y in (0, height - 1):
            edge_points.add(view[y][x])

res = max(area for coord, area in Counter(flatten(view)).items() if not coord in edge_points)
print(res)