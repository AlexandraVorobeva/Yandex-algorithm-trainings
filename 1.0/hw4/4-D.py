from collections import Counter

n = int(input())
seq = list(map(int, input().strip().split()))
k = int(input())
but = list(map(int, input().strip().split()))

b = dict(Counter(but))

for i in range(n):
    num = i +1
    if seq[i] < b[num]:
        print("YES")
    else:
        print("NO")