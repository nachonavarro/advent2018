from one import manhattan, coords, width, height

within_dist = lambda point: sum(manhattan(point, coord) for coord in coords) < 10000
res = sum(1 for x in range(width) for y in range(height) if within_dist((x, y)))

print(res)