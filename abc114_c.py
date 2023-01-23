import sys
sys.setrecursionlimit(1000000)

def dfs(n):
    ret = 0
    for i in [3, 5, 7]:
        m = n * 10 + i

        if m > N:
            continue

        sm = str(m)
        if sm.count("3") > 0 and sm.count("5") > 0 and sm.count("7") > 0:
            ret += 1

        ret += dfs(m)

    return ret

N = int(input())
print(dfs(0))
