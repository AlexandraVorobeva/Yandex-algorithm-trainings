w, h, n = map(int, input().split())
l, r = 0, max(w, h) * n
while l < r:
    m = (l + r) // 2
    if (m // w) * (m // h) >= n:
        r = m
    else:
        l = m + 1
print(l)