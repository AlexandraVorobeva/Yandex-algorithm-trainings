def check_x3_gt0(x, params):
    a, b, c, d = params
    x3 = a * x ** 3 + b * x ** 2 + c * x + d
    return x3 >= 0

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

eps= 0.0000001
l = -10000000
r = 10000000
a, b, c, d = map(int, input().split())

if a >= 0:
    root3x = fbinsearch(l, r, eps, check_x3_gt0, (a, b, c, d))
else:
    root3x = fbinsearch(l, r, eps, check_x3_gt0, (-a, -b, -c, -d))
print(root3x)