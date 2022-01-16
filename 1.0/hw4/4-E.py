n = int(input())
d = {}
for _ in range(n):
    x,y = map(int, input().split())
    d[x] = d.get(x, list()) + [y]

height = 0

for x in d.keys():
    height += max(d[x])

print(height)