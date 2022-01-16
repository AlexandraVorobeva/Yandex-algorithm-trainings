n = int(input())
d = dict()

for _ in range(n):
    st = input().split(' ')
    d[st[0]] = st[1]

word = input()

for key, val in d.items():
    if word == key:
        print(val)
    if word == val:
        print(key)