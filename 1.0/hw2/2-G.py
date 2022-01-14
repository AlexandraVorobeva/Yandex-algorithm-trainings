import heapq
from operator import mul

seq = list(map(int, input().strip().split()))

smallest = heapq.nsmallest(2, seq)
biggest = heapq.nlargest(2, seq)
if mul(*smallest) > mul(*biggest):
    for small in sorted(smallest):
        print(small, end=' ')
else:
    for big in sorted(biggest):
        print(big, end=' ')