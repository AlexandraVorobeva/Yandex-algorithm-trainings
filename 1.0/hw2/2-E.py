def cow_champ():
    n = int(input())
    seq = list(map(int, input().strip().split()))

    res = []
    min_metrs = min(seq)
    max_metrs = max(seq)

    if n > 2:
        for i in range(1, n-1):
            if str(seq[i]).endswith('5'):
                if seq[i+1] == min_metrs:
                    for j in range(i):
                        if seq[j] == max_metrs:
                            res.append(seq[i])
    if not res:
        return 0
    else:
        seq.sort(reverse=True)
        ind = seq.index(max(res))
        return ind +1


print(cow_champ())