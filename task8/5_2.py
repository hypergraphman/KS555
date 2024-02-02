from itertools import product

words = [''.join(word) for word in product('ЭЛИНА', repeat=5)]

k = 0
for word in words:
    t = word.replace('Э', 'А').replace('И', 'А').replace('Л', 'Н')
    if 'НН' not in t and 'АА' not in t:
        k += 1
print(k)