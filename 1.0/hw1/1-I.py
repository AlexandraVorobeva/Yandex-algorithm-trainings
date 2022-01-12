a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


kirpich = sorted([a, b, c])

if (min(d, e) >= kirpich[0]) and (max(d, e) >= kirpich[1]):
    print("YES")
else:
    print("NO")