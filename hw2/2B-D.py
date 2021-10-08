def seat(lenght, n, seq):
    idx = 0
    for i in range(n):
        if seq[i] < lenght//2:
            idx = i
        if seq[i] == lenght//2 and lenght % 2 != 0:
            return seq[i]
    return str(seq[idx])+' '+str(seq[idx+1])


lenght, n = map(int, input().split())
seq = list(map(int, input().split()))
print(seat(lenght, n, seq))