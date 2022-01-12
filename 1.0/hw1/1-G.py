n, k, m = map(int, input().split())

item_from_blank = k // m
rest_from_blank = k % m
item = 0
if m <= k:
    while n >= k:
        blank = n // k
        item += (blank * item_from_blank)
        n = (n % k) + rest_from_blank * blank

print(item)