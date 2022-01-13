seq = list(map(int, input().strip().split()))
cnt = 0
for i in range(1, len(seq)-1):
    if (seq[i] > seq[i-1]) and (seq[i] > seq[i+1]):
        cnt +=1
print(cnt)