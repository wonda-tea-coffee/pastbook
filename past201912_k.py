import sys
sys.setrecursionlimit(1000000)

def euler(u, pa=-1):
    global idx

    L[u] = idx
    idx += 1
    for v in E[u]:
        if v != pa:
            euler(v, u)
    R[u] = idx

idx = 0
root = -1
N = int(input())
E = [[] for i in range(N+1)]
L = [-1] * (N+1)
R = [-1] * (N+1)

for i in range(1, N+1):
    pi = int(input())
    if pi == -1:
        root = i
    else:
        E[pi].append(i)
        E[i].append(pi)

euler(root)

Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    if L[b] <= L[a] and R[a] <= R[b]:
        print("Yes")
    else:
        print("No")
