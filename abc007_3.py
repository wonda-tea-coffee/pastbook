from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
G = []
for i in range(R):
    G.append(input())
F = [[False] * C for i in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

queue = deque()
queue.append((sy, sx, 0))
F[sy][sx] = True

while len(queue) > 0:
    y, x, c = queue.popleft()

    if y == gy and x == gx:
        print(c)
        break

    nc = c + 1
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + d[0]
        nx = x + d[1]
        if ny >= 0 and ny < R and nx >= 0 and nx < C and not F[ny][nx] and G[ny][nx] == ".":
            F[ny][nx] = True
            queue.append((ny, nx, nc))
