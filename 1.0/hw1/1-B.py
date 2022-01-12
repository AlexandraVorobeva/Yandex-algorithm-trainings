a = int(input())
b = int(input())
c = int(input())

arglist = (a,b,c)

mx = max(arglist)
sides_sum = a+b+c

if min(arglist) <= 0:
    print('NO')
elif (mx >= sides_sum - mx):
    print('NO')
else:
    print('YES')