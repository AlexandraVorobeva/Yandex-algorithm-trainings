n = int(input())

d = dict()

for _ in range(n):
    languages = int(input())
    for leng in range(languages):
        lengu = input()
        if lengu in d:
            d[lengu] +=1
        else:
            d[lengu] = 1

every_knows = []
for key, val in d.items():
    if val == n:
        every_knows.append(key)
print(len(every_knows))
for ev in every_knows:
    print(ev)
print(len(d))
for key in d.keys():
    print(key)