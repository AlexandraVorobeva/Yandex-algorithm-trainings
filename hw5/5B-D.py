seq = list(input())
stack = []
is_good = True

for s in seq:
    if s == '(':
        stack.append(s)
    elif s == ')':
        if not stack:
            is_good = False
            break
        open_backet = stack.pop()
        if open_backet == '(' and s == ')':
            continue

if is_good and len(stack)==0:
    print('YES')
else:
    print('NO')