Input = [800, 600, 400, 200]
Compared_input = [500, 200, 400]


# for i in range(len(Input)):
#     if Input[i] in Compared_input:
#         Input[i] = 1  
#     else:
#         Input[i] = 0  

print(Input)  # [0, 0, 1, 1]


# Reverse Compared Input

for i in range(len(Input)):
    if Input[i] in Compared_input:
        Input[i] = 0


print(Input) 