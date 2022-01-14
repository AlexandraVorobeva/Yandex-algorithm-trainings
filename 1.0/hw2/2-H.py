import heapq
from functools import reduce
from operator import mul

seq = list(map(int, input().strip().split()))

biggest = heapq.nlargest(3, seq)
smallest = heapq.nsmallest(2, seq)
smallest.append((max(biggest)))
if reduce(mul, smallest, 1) > reduce(mul, biggest, 1):
    for sm in smallest:
        print(sm, end=' ')
else:
    for big in biggest:
        print(big, end=' ')