N, X = map(int, input().split())
w = []
for i in range(N):
    w.append(int(input()))

n = N // 2
l = w[:n]
r = w[n:]
wa = {}
wb = {}
for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i>>j & 1:
            sum += l[j]
    if sum in wa:
        wa[sum] += 1
    else:
        wa[sum] = 1

for i in range(1<<(N-n)):
    sum = 0
    for j in range(N-n):
        if i>>j & 1:
            sum += r[j]
    if sum in wb:
        wb[sum] += 1
    else:
        wb[sum] = 1

ans = 0
for wai in wa:
    wbi = X - wai
    if wbi in wb:
        ans += wa[wai] * wb[wbi]

print(ans)
