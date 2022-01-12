with open('input.txt', 'r') as f:
    text = f.readlines()
text = ' '.join(text)
all_words = set(text.strip().split())
print(len(all_words))