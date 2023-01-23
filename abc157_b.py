def is_bingo():
    for i in range(M):
        yoko = True
        tate = True
        for j in range(M):
            yoko &= F[i][j]
            tate &= F[j][i]
        if yoko or tate:
            return True

    nnm1 = True
    nnm2 = True
    for i in range(M):
        nnm1 &= F[i][i]
        nnm2 &= F[i][M - i - 1]

    return nnm1 or nnm2

A = []
M = 3
for i in range(M):
    A.append(list(map(int, input().split())))
F = [[False for i in range(M)] for i in range(M)]

N = int(input())
for i in range(N):
    bi = int(input())
    for j in range(M):
        for k in range(M):
            if bi == A[j][k]:
                F[j][k] = True

# print(F)

if is_bingo():
    print("Yes")
else:
    print("No")
