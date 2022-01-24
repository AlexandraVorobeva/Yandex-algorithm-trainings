stud, teach = map(int, input().strip().split())
stud_check = []


for i in range(teach):
    a, b = map(int, input().strip().split())
    sud = list(range(a, b+1))
    for su in sud:
        if su not in stud_check:
            stud_check.append(su)

print(stud - len(stud_check))