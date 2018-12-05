from one import create_timetable

guard, ts = max(create_timetable().items(), key=lambda info: max(info[1]))
res = guard * ts.index(max(ts))
print(res)