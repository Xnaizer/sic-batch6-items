input = [1,2,3,4,5,6,7,8,9,10]

genap = list(filter(lambda x: x % 2 == 0, input))

print(genap)

ganjil = list(filter(lambda x: x % 2 == 1, input))

print(ganjil)
