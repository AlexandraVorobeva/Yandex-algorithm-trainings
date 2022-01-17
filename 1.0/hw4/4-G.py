d = {}
operations = list()


with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        operations.append(line.strip().split())

for oper in operations:
    if oper[0] == "DEPOSIT":
        if oper[1] not in d:
            d[oper[1]] = int(oper[2])
        elif oper[1] in d:
            d[oper[1]] += int(oper[2])

    elif oper[0] == "WITHDRAW":
        if oper[1] not in d:
            c = int(oper[2])
            d[oper[1]] = -c
        else:
            d[oper[1]] -= int(oper[2])

    elif oper[0] == "BALANCE":
        if oper[1] not in d:
            print("ERROR")
        else:
            print(d[oper[1]])

    elif oper[0] == "TRANSFER":
        if oper[1] not in d:
            c = int(oper[3])
            d[oper[1]] = -c
        elif oper[1] in d:
            d[oper[1]] -= int(oper[3])

        if oper[2] not in d:
            d[oper[2]] = int(oper[3])
        elif oper[2] in d:
            d[oper[2]] += int(oper[3])

    elif oper[0] == "INCOME":
        for key, val in d.items():

            if val > 0:
                d[key] = int(val/100 * (100 + int(oper[1])))