serial = int(open('in.txt').read())
power = lambda x, y: (x + 10) * ((x + 10) * y + serial) // 100 % 10 -5

def summed_area_table(size):
    view = [[0] * size for _ in range(size)]
    for y in range(size):
        for x in range(size):
            if x == 0 or y == 0:
                view[y][x] = power(x, y)
            else:
                view[y][x] = power(x, y) + view[y - 1][x] + view[y][x - 1] - view[y - 1][x - 1]
    return view

def largest_submatrix(size):
    best_x = best_y = largest = 0
    for y in range(total_size - size):
        for x in range(total_size - size):
            total = view[y][x] - view[y + size][x] - view[y][x + size] + view[y + size][x + size]
            if total > largest:
                largest = total
                best_x, best_y = x, y
    return best_x, best_y, largest

total_size = 300
view = summed_area_table(total_size)
best_x, best_y, best_submatrix = largest_submatrix(3)
print(best_x + 1, best_y + 1, best_submatrix)