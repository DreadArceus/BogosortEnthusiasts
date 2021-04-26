import random
from itertools import permutations

arr = [1, 2, 3]
random.shuffle(arr)

size = 3
data = []
while size < 20:
    i = 0
    arrPerms = [list(p) for p in permutations(range(1, size))]
    for p in arrPerms:
        if p == arr:
            break
        i += 1
        if i > 10000000 and i % 10000000 == 0:
            print(f'Interim Report at {i}')
    print(f'Size: {size}, Done after {i}\n')
    data.append((size, i))
    size += 1
    arr.append(size)
    random.shuffle(arr)

print(f'Final report: {data}')
