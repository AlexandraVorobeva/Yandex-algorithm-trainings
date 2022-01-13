seq = list(map(int, input().split()))

flag = True

for i in range(len(seq)-1):
    if seq[i] >= seq[i+1]:
        flag = False

print("NO" if not flag else 'YES')