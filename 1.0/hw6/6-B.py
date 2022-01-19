def isInSeq(n, seq):
    l, r = 0, len(seq) - 1
    while r - l > 1:
        m = (l + r) // 2
        if n <= seq[m]:
            r = m
        else:
            l = m
    if seq[r] - n < n - seq[l]:
        return seq[r]
    return seq[l]


n, k = map(int, input().strip().split())
seq_n = list(map(int, input().strip().split()))
seq_k = list(map(int, input().strip().split()))
for se in seq_k:
    print(isInSeq(se, seq_n))