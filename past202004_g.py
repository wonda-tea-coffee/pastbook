import string
from collections import deque, defaultdict

Q = int(input())
dq = deque()

for i in range(Q):
    q = input().split()
    if q[0] == "1":
        dq.append((q[1], int(q[2])))
    else:
        d = int(q[1])
        ch_cnt = defaultdict(lambda: 0)
        count_sum = 0
        while len(dq) > 0:
            ch, count = dq.popleft()
            if count_sum + count < d:
                count_sum += count
                ch_cnt[ch] += count
            else: # count_sum + count >= d
                e = d - count_sum
                ch_cnt[ch] += e
                dq.appendleft((ch, count - e))
                break

        ans = 0
        for c in list(string.ascii_lowercase):
            ans += ch_cnt[c]**2
        print(ans)
