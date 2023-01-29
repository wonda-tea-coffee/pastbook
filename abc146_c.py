def d(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret

A, B, X = map(int, input().split())

ans = 0
for dn in range(18, 0, -1):
    n = (X - B*dn) // A
    # print("dn = ", dn, ", n = ", n)
    m = 0
    if d(n) > dn:
        m = 10**dn - 1
    elif d(n) == dn:
        m = n
    ans = max(ans, min(m, 10**9))

print(ans)

# A*n + B*d_n <= X
# A*n <= X - B*d_n
# n = (X - B*d_n) // A
