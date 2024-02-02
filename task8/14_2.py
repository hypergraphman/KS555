from itertools import permutations

words = [''.join(word) for word in permutations('ЭМИЛЬ', r=5)]

a = set()
for word in words:
    if word[0] != 'Ь' and 'ИЭ' not in word:
        a.add(word)
print(len(a))