with open("input.txt", "r") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
res = dict.fromkeys([l[0] for l in lines], 0)
for l in lines:
    res[l[0]] += int(l[1])
for k in sorted(res.keys()):
    print(k, res[k])