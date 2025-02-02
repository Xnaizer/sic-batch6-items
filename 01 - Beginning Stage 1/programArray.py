# Buat sebuah program yang jika kita berikan sebuah
# input array seperti
# [1,2,3,4,5] maka akan menghasilkan output [1,4,9,16,25]!

array = [1,2,3,4,5]

for i in range(len(array)):
    array[i] = array[i] * array[i]

print(array) # [1, 4, 9, 16, 25]

result = map(lambda x: x * x, array)
print(list(result))