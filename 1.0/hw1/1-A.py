troom, tcond = map(int, input().strip().split())
real = input()
res = None

if real == 'freeze':
    if troom <= tcond:
        res = troom
    else:
        res = tcond
if real == 'heat':
    if troom >= tcond:
        res = troom
    else:
        res = tcond
if real == 'auto':
    res = tcond
if real == 'fan':
    res = troom

print(res)