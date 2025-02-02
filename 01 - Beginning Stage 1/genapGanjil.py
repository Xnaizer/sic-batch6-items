
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(array)):
    if array[i] % 2 == 0:
        array[i] = "Genap"
    else:
        array[i] = "Ganjil"

print(array) # ['Genap', 'Ganjil', 'Genap', 'Ganjil', 'Genap', 'Ganjil', 'Genap', 'Ganjil', 'Genap', 'Ganjil']