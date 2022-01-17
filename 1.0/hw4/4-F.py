d = {}

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        name, prod, cnt = line.strip().split()
        if name in d:
            if prod in d[name]:
                d[name][prod] += int(cnt)
            else:
                d[name][prod] = int(cnt)
        else:
            d[name] = {prod: int(cnt)}


list_key_name = list(d.keys())
list_key_name.sort()

for i in list_key_name:
    print(i + ':')
    list_prod_name = list(d[i].keys())
    list_prod_name.sort()
    for j in list_prod_name:
        print(j, d[i][j])