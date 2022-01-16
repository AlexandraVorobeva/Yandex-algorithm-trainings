from itertools import chain

wordcnt = {}

with open("input.txt") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    seq = list(chain(*lines))
    for se in seq:
        wordcnt[se] = wordcnt.get(se, 0) +1

ans = []
for w in wordcnt:
    ans.append((-wordcnt[w], w))

ans.sort()
print(ans[0][1])