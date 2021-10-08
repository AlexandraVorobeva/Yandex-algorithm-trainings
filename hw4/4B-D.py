partyes = []
sumcnt = 0
i = 0
with open("input.txt", "r") as f:
    for line in f:
        words = line.split()
        cnt = int(words[-1])
        partyname = ' '.join(words[:-1])
        partyes.append([partyname, cnt, i])
        sumcnt +=cnt
        i +=1

f = sumcnt / 450
free = 450
for i in range(len(partyes)):
    party = partyes[i]
    party.append(party[1] // f)
    free -= party[1] // f
    party.append(party[1] % f)

partyes.sort(key= lambda x: x[4], reverse=True)
for i in range(int(free)):
    partyes[i][3] +=1

partyes.sort(key= lambda x: x[2])

for party in partyes:
    print(party[0], int(party[3]))