n = int(input())
seq = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))


def lbinsearch(x, seq):
    l = 0
    r = len(seq)
    while l < r:
        m = (l + r)//2
        if seq[m] < x:
            l = m +1
        else:
            r = m
    return l

def rbinsearch(x, seq):
    l = 0
    r = len(seq)
    while l < r:
        m = (l + r) // 2
        if seq[m] > x:
            r = m
        else:
            l = m +1
    return l

seq_set = set(seq)
ans = []

for order in orders:
    if order in seq_set:
        ans.append([lbinsearch(order, seq) + 1, rbinsearch(order, seq)])
    else:
        ans.append([0, 0])

for _ in ans:
    print(*_)