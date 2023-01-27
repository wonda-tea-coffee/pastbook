N = int(input())
s = []
for i in range(N):
    ai, bi = map(int, input().split())
    s.append((-ai-bi, ai, bi))

s.sort()
ans = 0
for i in range(N):
    _, a, b = s[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
