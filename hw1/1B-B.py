n, i, j = map(int, input().split())
dist1 = abs(j - i) -1
dist2 = n - 2 - dist1
print(min(dist1, dist2))