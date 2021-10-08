code = int(input())
ind = int(input())
checker = int(input())


if ind == 0:
    if code != 0:
        res = 3
    else:
        res = checker
elif ind == 1:
    res = checker
elif ind == 4:
    if code != 0:
        res = 3
    else:
        res = 4
elif ind == 6:
    res = 0
elif ind == 7:
    res = 1
else:
    res = ind

print(res)