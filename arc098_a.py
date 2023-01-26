N = int(input())
S = input()
sumW = []
sumE = []
cntW = 0
cntE = 0
for i in range(N):
    if S[i] == "W":
        cntW += 1
    else:
        cntE += 1
    sumW.append(cntW)
    sumE.append(cntE)

ans = 10**100
for i in range(N):
    lw, re = 0, 0

    if i > 0:
        lw = sumW[i-1]

    if i < N-1:
        re = sumE[N-1] - sumE[i]

    ans = min(ans, lw + re)

print(ans)
