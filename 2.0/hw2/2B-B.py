d = list(map(int, input().split()))
left = [0] * len(d)
shoppos = -20

for i in range(len(d)):
    if d[i] == 2:
        shoppos = i
    if d[i] == 1:
        left[i] = i - shoppos
ans = 0
shoppos = 30

for i in range(len(d)-1, -1, -1):
    if d[i] == 2:
        shoppos = i
    if d[i] == 1:
        mindist = min(shoppos - i, left[i])
        ans = max(ans, mindist)
print(ans)