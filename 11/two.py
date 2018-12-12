from one import largest_submatrix

total_size, largest, best_submatrix = 300, 0, 0
for submatrix_size in range(1, total_size):
    x, y, total = largest_submatrix(submatrix_size)
    if total > largest:
        best_x, best_y = x, y
        largest = total
        best_submatrix = submatrix_size

print(best_x + 1, best_y + 1, best_submatrix)