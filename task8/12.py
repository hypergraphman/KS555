from itertools import product

words = [''.join(x) for x in product('01234', repeat=5)]
k = 0
for n in words:
    if n[0] != '0' and len(set(n)) == 4 and '11' not in n and '00' not in n and '22' not in n and '33' not in n and '44' not in n:
        k += 1
print(k)