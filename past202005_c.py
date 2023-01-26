import math

A, R, N = map(int, input().split())

if (N-1)*math.log(R, 10) + math.log(A, 10) > 9:
    print("large")
else:
    print(A * R**(N-1))
