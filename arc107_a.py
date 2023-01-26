A, B, C = map(int, input().split())

print(A * (A+1) * B * (B+1) * C * (C+1) // 8 % 998244353)
