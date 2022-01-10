gen1 = input()
gen2 = input()

set2 = set()
for i in range (len(gen2) - 1):
	set2.add(gen2[i:i + 2])

cnt = 0
for i in range(len(gen1) - 1):
	if gen1[i:i + 2] in set2:
		cnt += 1
print(cnt)

