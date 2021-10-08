from itertools import chain

wordcnt = {}

with open("input.txt") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    words = list(chain(*lines))
    for word in words:
        wordcnt[word] = wordcnt.get(word, 0) + 1

ans = []
for w in wordcnt:
    ans.append((-wordcnt[w], w))

ans.sort()
for cnt, word in ans:
    print(word)