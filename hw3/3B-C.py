spis = list(map(int, input().split()))
res = list()
for i in spis:
    if spis.count(i) == 1:
        res.append(i)
for i in res:
	print(i)