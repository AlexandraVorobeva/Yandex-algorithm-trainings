n, m = map(int, input().strip().split())
segment = []
res = []

for i in range(n):
    a, b = map(int, input().strip().split())
    if a > b:
        a, b = b, a
    segment.append((a,b))

points = tuple(map(int, input().strip().split()))
for point in points:
    cnt = 0
    for seg in segment:
        if seg[0] < point < seg[1]:
            cnt += 1
    res.append(cnt)

for re in res:
    print(re, end=' ')