import sys
sys.setrecursionlimit(1000000)

def calc(g1, g2, g3):
    ret = 0
    for g in [g1, g2, g3]:
        for i in range(len(g)):
            for j in range(i+1, len(g)):
                ret += h[(g[i], g[j])]
    return ret

def dfs(g1, g2, g3, n):
    global ans

    if n > N:
        ans = max(ans, calc(g1, g2, g3))
        return

    for g in [g1, g2, g3]:
        g.append(n)
        dfs(g1, g2, g3, n+1)
        g.pop()

N = int(input())
h = {}

for i in range(1, N):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        h[(i, i+j+1)] = a[j]
        h[(i+j+1, i)] = a[j]
h[(N, N-1)] = h[(N-1, N)]

ans = -10**100

dfs([], [], [], 1)

print(ans)
