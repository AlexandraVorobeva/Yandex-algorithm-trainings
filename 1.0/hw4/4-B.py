from itertools import chain

d = dict()

with open("input.txt") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    seq = list(chain(*lines))
    for se in seq:
        if se in d.keys():
            d[se] +=1
            print(d[se])
        else:
            print(0)
            d[se] = 0