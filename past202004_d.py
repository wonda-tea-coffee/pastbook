import string
import re

S = input()
L = list(string.ascii_lowercase) + [".", ""]
M = len(L)
ans = set()
for l in range(1, 4):
    for i1 in range(M):
        for i2 in range(M):
            for i3 in range(M):
                T = L[i1] + L[i2] + L[i3]
                if T == "":
                    continue
                if re.search(T, S):
                    # print(T)
                    ans.add(T)

print(len(ans))
