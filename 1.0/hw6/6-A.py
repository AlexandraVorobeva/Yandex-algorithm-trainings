def isInSeq(n, seq):
    l, r = 0, len(seq) - 1
    while l < r:
        m = (l + r) // 2
        if n <= seq[m]:
            r = m
        else:
            l = m + 1
    if seq[l] == n:
        return 'YES'
    return 'NO'


N, K = map(int, input().split())
seq1 = sorted(map(int, input().split()))
for n in map(int, input().split()):
    print(isInSeq(n, seq1))