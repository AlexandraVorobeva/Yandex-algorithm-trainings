n = int(input())
events = [] * 2 * n
for num in range(n):
    l, r = list(map(int, input().strip().split()))
    events.append([l, 1])
    events.append([l + r, -1])

events.sort()


res = 0
cargo = 0

for time, code in events:
    if code == -1:
        cargo -= 1
    if code == 1:
        cargo += 1
    res = max(res, cargo)
print(res)