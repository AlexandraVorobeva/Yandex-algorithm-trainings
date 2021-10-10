m = int(input())
segr = []
l, r = map(int, input().split())
while l != 0 or r !=0:
    if r > 0 and l < m:
        segr.append((l, r))
    l, r = map(int, input().split())

segr.sort()
ans = []
nowright = 0
nextright = 0
nowbest = 0, 0
for seg in segr:
    if seg[0] > nowright:
        ans.append(nowbest)
        nowright = nextright
        if nowright >= m:
            break
    if seg[0] <= nowright and seg[1] > nextright:
        nextright = seg[1]
        nowbest = seg
if nowright < m:
    nowright = nextright
    ans.append(nowbest)
if nowright < m:
    print('No solution')
else:
    print(len(ans))
    for seg in ans:
        print(*seg)