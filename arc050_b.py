R, B = map(int, input().split())
x, y = map(int, input().split())

def is_ok(n):
    # 花束1を作った回数: a
    # 花束2を作った回数: b
    # a + b = n
    #     b = n - a
    # a*x + b <= R
    # a*x + n - a <= R
    # a*x - a <= R - n
    # a(x - 1) <= R - n
    # a <= (R - n)/(x - 1)
    #
    # a = n - b
    # a + b*y <= B
    # n - b + b*y <= B
    # n + b(y - 1) <= B
    # b <= (B - n)/(y - 1)
    r = R - n
    b = B - n
    if r < 0 or b < 0:
        return False

    m = r//(x-1) + b//(y-1)
    return m >= n

ok = 0
ng = 10**18+1

while abs(ok-ng) > 1:
    # print(ok, ng)
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
