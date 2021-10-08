with open("input.txt", "r") as f:
    seq = list(map(int, f.readlines()))[:-1]

maximum = seq[0]
cnt = 0
for i in seq:
    if maximum == i:
        cnt += 1
    if i > maximum:
        cnt = 1
        maximum = i
print(cnt)