spis = list(map(int, input().split()))
unic = set()
for s in spis:
    if s in unic:
        print("YES")
    else:
        print("NO")
        unic.add(s)