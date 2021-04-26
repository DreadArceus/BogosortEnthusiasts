import random

arr = [1, 2, 3]
arrSorted = arr.copy()
arr.reverse()

size = 3
data = []
while size < 20:
    i = 0
    while arr != arrSorted:
        random.shuffle(arr)
        i += 1
        if i > 10000000 and i % 10000000 == 0:
            print(f'Interim Report at {i}')
    print(f'Size: {size}, Done after {i}')
    data.append((size, i))
    size += 1
    arr.append(size)
    arr.reverse()
    arrSorted.append(size)

print(f'Final report: {data}')
