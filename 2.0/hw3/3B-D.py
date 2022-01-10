n = int(input())
pos = set(range(1, n + 1))
s = input().strip()
while s != 'HELP':
    nums = set(map(int, s.split()))
    s = input().strip()
    if s == "YES":
        pos.intersection_update(nums)
    else:
        pos.difference_update(nums)
    s = input().strip()
print(*sorted(pos))