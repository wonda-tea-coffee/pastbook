import sys
from collections import deque

N, X, Y = map(int, input().split())
F = set()
for i in range(N):
    xi, yi = map(int, input().split())
    F.add((xi, yi))

queue = deque()
queue.append((0, 0, 0))
C = {}

while len(queue) > 0:
    x, y, c = queue.popleft()

    # print("(%i, %i): %i" % (x, y, c))

    if x == X and y == Y:
        print(c)
        sys.exit(0)

    nc = c + 1
    for d in [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + d[0]
        ny = y + d[1]
        if not (nx, ny) in F and (not (nx, ny) in C or nc < C[(nx, ny)]) and abs(nx) <= 201 and abs(ny) <= 201:
            C[(nx, ny)] = nc
            queue.append((nx, ny, nc))

print(-1)
