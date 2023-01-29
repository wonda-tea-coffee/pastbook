N = int(input())
Q = int(input())

row = list(range(N))
col = list(range(N))
ans = []

flag = False
for i in range(Q):
    q = list(map(int, input().split()))

    t = q[0]
    if t != 3:
        A, B = q[1], q[2]
        A -= 1
        B -= 1

    if t == 1:
        row[A], row[B] = row[B], row[A]
    elif t == 2:
        col[A], col[B] = col[B], col[A]
    elif t == 3:
        row, col = col, row
        flag = not flag
    else:
        if flag:
            ans.append(N*col[B] + row[A])
        else:
            ans.append(N*row[A] + col[B])

for a in ans:
    print(a)