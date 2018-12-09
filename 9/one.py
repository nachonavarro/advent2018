import re
from collections import deque

players, points = (int(p) for p in re.search(r'(\d+) .* (\d+)', open('in.txt').read()).groups())

def play(players, points):
    board, scores = deque(), {}
    for marble in range(points + 1):
        multiple = marble and marble % 23 == 0
        if multiple:
            board.rotate(7)
            scores[marble % players] = scores.get(marble % players, 0) + marble + board.pop()
        board.rotate(-1)
        if not multiple:
            board.append(marble)
    return max(scores.values())

res = play(players, points)
print(res)
