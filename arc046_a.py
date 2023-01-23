N = int(input()) - 1
print("".join([str(N % 9 + 1) for i in range(N // 9 + 1)]))
