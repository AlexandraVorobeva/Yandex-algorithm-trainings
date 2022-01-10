cou = int(input())
reply = [0] * cou
topics = [''] * cou

for i in range(cou):
    n = int(input())
    if n == 0:
        reply[i] = i
        topics[i] = input()
        input()
    else:
        reply[i] = reply[n - 1]
        input()

cntreplys = {}
for rep in reply:
    cntreplys[rep] = cntreplys.get(rep, 0) + 1

ans = []
for topic in cntreplys:
    ans.append((-cntreplys[topic], topic))
print(topics[min(ans)[1]])