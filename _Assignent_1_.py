num_1 = 1
num_2 = 2
for i in range(10):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")