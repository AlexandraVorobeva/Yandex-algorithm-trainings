a = int(input())
b = int(input())
c = int(input())
x = 0

if c < 0:
    print('NO SOLUTION')
else:
    if a==0:
        if b<0:
            print('NO SOLUTION')
        elif b == c**2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        x = (c**2-b)/a
        if (a*x+b >= 0) and (x==int(x)):
            print(int(x))
        else:
            print('NO SOLUTION')