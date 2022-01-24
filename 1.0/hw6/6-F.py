N, x, y = map(int, input().split())
if x > y:
    x, y = y, x
l, r = x, y * N
while l < r:
    m = (l + r) // 2
    if (m - x) // x + (m - x) // y >= N - 1:
        r = m
    else:
        l = m + 1
print(l)