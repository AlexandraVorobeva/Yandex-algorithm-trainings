n = int(input())
seq = list(map(int, input().strip().split()))
orders_num = int(input())
orders = []
for order in range(orders_num):
    l, r = map(int, input().split())
    orders.append([l, r])

seq.sort()

def lbs(x, sequence):
    l = 0
    r = len(sequence)
    while l < r:
        m = (l + r) // 2
        if seq[m] < x:
            l = m + 1
        else:
            r = m
    return l


def rbs(x, sequence):
    l = 0
    r = len(sequence)
    while l < r:
        m = (l + r) // 2
        if seq[m] > x:
            r = m
        else:
            l = m + 1
    return l


ans = []

for order in orders:
    ans.append(rbs(order[1], seq) - lbs(order[0], seq))