from one import play

first = play(100)
diff = play(200) - play(100) # Stable difference
res = first + diff * (50_000_000_000 - 100) / 100
print(res)