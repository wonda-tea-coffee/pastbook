N = int(input())
s = []
for i in range(N):
    ai, bi = map(int, input().split())
    s.append((bi, ai))

s.sort()
# print(s)
t, ans = 0, 0
for si in s:
    b, a = si
    if t < a:
        ans += 1
        t = b
print(ans)
