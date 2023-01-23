S = input()

cnta = S.count("a")
cntb = S.count("b")
cntc = S.count("c")
cntm = max([cnta, cntb, cntc])

if cntm == cnta:
    print("a")
elif cntm == cntb:
    print("b")
else:
    print("c")
