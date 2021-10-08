n = int(input())
parcels = []

for i in range(n):
    parcels.append(tuple(map(int, input().split())))

d = dict()
for p in parcels:
    if p[0] in d.keys():
        d[p[0]] += p[1]
    else:
        d.update({p[0]: p[1]})

for k in sorted(d.keys()):
    print(k, d[k])