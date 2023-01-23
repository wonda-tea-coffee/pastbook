import sys

c = []
for i in range(3):
    c.append(list(map(int, input().split())))

a = [0] * 3
b = [0] * 3

# c1_1(= a1 + b1), c1_2(= a1 + b2), c1_3(= a1 + b3)
# c2_1(= a2 + b1), c2_2(= a2 + b2), c2_3(= a2 + b3)
# c3_1(= a3 + b1), c3_2(= a3 + b2), c3_3(= a3 + b3)

b[2] = (c[0][0] - c[1][1] - c[0][2] + c[1][2]) // 2
a[0] = c[0][2] - b[2]
a[1] = c[1][2] - b[2]
a[2] = c[2][2] - b[2]
b[0] = c[1][0] - a[1]
b[1] = c[1][1] - a[1]

for i in range(3):
    for j in range(3):
        if a[i] + b[j] != c[i][j]:
            print("No")
            sys.exit(0)

print("Yes")
