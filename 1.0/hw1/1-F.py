a1, a2, b1, b2 = map(int, input().split())
size = []

size1 = (a1 + b1) * max(a2, b2)
size.append((size1, a1 + b1, max(a2, b2)))

size2 = (a1 + b2) * max(a2, b1)
size.append((size2, a1 + b2, max(a2, b1)))

size3 = (a2 + b1) * max(a1, b2)
size.append((size3, a2 + b1, max(a1, b2)))

size4 = (a2 + b2) * max(a1, b1)
size.append((size4, a2 + b2, max(a1, b1)))
size = sorted(size)
print(size[0][1], size[0][2])