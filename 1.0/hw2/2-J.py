n = int(input())
first = float(input())

maxx=4000
minx=30


for _ in range(1, n):
    t, s = input().split(" ")
    t = float(t)
    x = (first + t) / 2.
    if first == t:
        continue
    elif (first < t and s == 'closer') or (first > t and s == 'further'):
        minx = max(x, minx)
    else:
        maxx = min(x, maxx)
    first = t
print(minx, maxx)