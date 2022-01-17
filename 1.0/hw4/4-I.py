n = int(input())
dictionary = {}

res = 0

for _ in range(n):
    s = input()
    s_lower = s.lower()
    if s_lower not in dictionary:
        dictionary[s_lower] = set()
    dictionary[s_lower].add(s)

words_of_Peta = input()
for word in words_of_Peta.split():
    word_lower = word.lower()
    if word_lower in dictionary:
        if word not in dictionary[word_lower]:
            res += 1
    else:
        stresses = 0
        for c in word:
            if c.isupper():
                stresses +=1
        if stresses != 1:
            res += 1

print(res)