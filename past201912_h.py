N = int(input())
C = list(map(int, input().split()))
Q = int(input())
m2 = min(C[::2])
m3 = min(C)
sum1 = [0] * N
sum2 = 0
sum3 = 0
for i in range(Q):
    S = list(map(int, input().split()))
    # print("Q%i:" % (i + 1), S)
    # print("C:", C)
    if S[0] == 1:
        x = S[1] - 1
        a = S[2]
        d = C[x] - sum1[x] - sum3
        if x % 2 == 0:
            d -= sum2
        if d >= a:
            d -= a
            sum1[x] += a
            if x % 2 == 0 and d < m2:
                m2 = d
            if d < m3:
                m3 = d
    else:
        a = S[1]
        if S[0] == 2:
            if m2 >= a:
                m2 -= a
                sum2 += a

                if m3 > m2:
                    m3 = m2
        elif S[0] == 3:
            if m3 >= a:
                m2 -= a
                m3 -= a
                sum3 += a

    # print("m2:", m2)
    # print("m3:", m3)
    # print("sum1:", sum1)
    # print("sum2:", sum2)
    # print("sum3:", sum3)
    # print("ans:", sum(sum1) + sum2 + sum3)

# print("Ans:")
print(sum(sum1) + sum2 * ((N + 1) // 2) + sum3 * N)
