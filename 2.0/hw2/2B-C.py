def repair(seq):
    price = 0
    for i in range(len(seq)//2):
        if seq[i] != seq[len(seq)-i-1]:
            price += 1
    return price


seq = input()
print(repair(seq))