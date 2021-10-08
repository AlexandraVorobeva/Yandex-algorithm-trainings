n, q = map(int,input().split())
seq = list(map(int,input().strip().split()))

pref_sums = [0] * (n + 1)

for i in range(1, n +1):
    pref_sums[i] = pref_sums[i -1] + seq[i -1]

for j in range(2, q + 2):
    from_index, to_index = map(int, input().split())
    print(pref_sums[to_index] - pref_sums[from_index - 1])