m = int(input())
wits = []
for _ in range(m):
    wits.append(set(input().strip()))
n = int(input())
nums = []
maxwitcnt = 0
for i in range(n):
    num = input().strip()
    numset = set(num)
    witcnt = 0
    for wit in wits:
        if wit <= numset:
            witcnt += 1
    nums.append((num, witcnt))
    maxwitcnt = max(maxwitcnt, witcnt)
ans = []
for num in nums:
    if num[1] == maxwitcnt:
        ans.append(num[0])
print('\n'.join(ans))