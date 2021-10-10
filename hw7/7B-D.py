n, m = map(int, input().split())
kittens = list(map(int, input().split()))

events = [(0, 0, 0)] * (2 * m + n)
lines = [[0, 0, 0]] * m

i = 0

for kitty in kittens:
    events[i] = (kitty, 0, -1)
    i += 1

for j in range(m):
    l, r = map(int, input().split())
    lines[j] = [l, r, 0]
    events[i] = (l, -1, j)
    events[i + 1] = (r, 1, j)
    i += 2

events.sort()
kittens_count = 0

for event in events:
    if event[1] == -1:
        lines[event[2]][2] = kittens_count
    elif event[1] == 1:
        lines[event[2]][2] = kittens_count - lines[event[2]][2]
    else:
        kittens_count += 1

print(' '.join([str(elem[2]) for elem in lines]))