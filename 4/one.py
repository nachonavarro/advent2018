import re

parse_time  = lambda ts: int(re.search(r'\[.* ..:(..)\]', ts).groups()[0])
parse_guard = lambda ts: int(re.search(r'#(\d+)', ts).groups()[0])

def create_timetable():
    timetable = {}
    for ts in sorted(open('in.txt')):
        if 'Guard' in ts:
            new_guard = parse_guard(ts)
            if new_guard not in timetable:
                timetable[new_guard] = [0] * 60
        elif 'asleep' in ts:
            asleep = parse_time(ts)
        elif 'wakes' in ts:
            awake = parse_time(ts)
            for minute in range(asleep, awake):
                timetable[new_guard][minute] += 1
    return timetable

guard, ts = max(create_timetable().items(), key=lambda info: sum(info[1]))
res = guard * ts.index(max(ts))
print(res)