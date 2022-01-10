def readandnum():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i + 1)
    x.sort()
    return x


n, m = map(int, input().split())
x = readandnum()
y = readandnum()
ynum = 0
ans = [0] * (n + 1)
cnt = 0
for pupils, xnum in x:
    while (ynum < len(y)) and (y[ynum][0] < pupils +1):
        ynum += 1
    if ynum == len(y):
        break
    ans[xnum] = y[ynum][1]
    ynum += 1
    cnt +=1
print(cnt)
print(*ans[1:])