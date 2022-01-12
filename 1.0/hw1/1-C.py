n = input()
a = input()
b = input()
c = input()

numbers = (n, a,b,c)
just_num = []

for num in numbers:
    num = ''.join([ch for ch in num if ch not in ('+-()')])
    nlen = len(num)

    if nlen == 11:
        just_num.append(num[1:])
    elif nlen == 8:
        num = '495' + num[1:]
        just_num.append(num)
    elif nlen == 7:
        num = '495' + num
        just_num.append(num)

etal = just_num[0]
all_tel = just_num[1::]
for tel in all_tel:
    if tel == etal:
        print('YES')
    else:
        print('NO')