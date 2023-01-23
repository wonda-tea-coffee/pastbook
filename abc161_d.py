import sys
sys.setrecursionlimit(1000000)

def dfs(x):
    global ans, ln

    if x <= M:
        ln.append(x)
        ans += 1

    d = x % 10
    if x * 10 + d <= M:
        dfs(x * 10 + d)
    if d > 0 and x * 10 + d - 1 <= M:
        dfs(x * 10 + d - 1)
    if d < 9 and x * 10 + d + 1 <= M:
        dfs(x * 10 + d + 1)

ans = 0
ln = []
K = int(input())
M = 10**10
for i in range(1, 10):
    dfs(i)

print(sorted(ln)[K - 1])
