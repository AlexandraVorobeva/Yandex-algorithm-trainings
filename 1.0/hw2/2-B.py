def type_seq():
    seq = []
    flag = True
    while flag:
        temp = int(input())
        if temp == -2000000000:
            flag = False
        else:
            seq.append(temp)

    if len(set(seq)) == 1:
        return 'CONSTANT'

    asce, we_asce, des, we_des = 0, 0, 0, 0
    for i in range(1, len(seq)):
        if seq[i-1] < seq[i]:
            asce +=1
        if seq[i - 1] <= seq[i]:
            we_asce += 1
        if seq[i - 1] > seq[i]:
            des += 1
        if seq[i - 1] >= seq[i]:
            we_des += 1

    if asce == len(seq) - 1:
        return 'ASCENDING'
    elif we_asce == len(seq) - 1:
        return 'WEAKLY ASCENDING'
    elif des == len(seq) - 1:
        return 'DESCENDING'
    elif we_des == len(seq) - 1:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'

print(type_seq())