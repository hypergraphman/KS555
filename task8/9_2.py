from itertools import product

words = [''.join(x) for x in product('stivbl', repeat=5)]
k = 0
for word in words:
    t = word.replace('t', 's').replace('v', 's').replace('l', 'b')
    if word.count('i') in (1, 3, 5) and t.count('s') == t.count('b'):
        k += 1
print(k)