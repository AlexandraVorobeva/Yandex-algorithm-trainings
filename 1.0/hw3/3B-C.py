ann_len, bor_len = map(int, input().split())

a = set()
b = set()
for _ in range(ann_len):
    a.add(int(input()))
for _ in range(bor_len):
    b.add(int(input()))

inter = a.intersection(b)
print(len(inter))
print(' '.join(map(str, sorted(inter))))
print(len(a-b))
print(' '.join(map(str, sorted(a-b))))
print(len(b-a))
print(' '.join(map(str, sorted(b-a))))