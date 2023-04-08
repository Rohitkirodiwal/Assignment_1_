# Write a python program to count the noumber of even and odd number from a series of numbers.
user = int(input("how many element will taken : "))
list=[]
for i in range(user):
    x = int(input())
    list.append(x)
print(list)


# sample_no_lst = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for list in list:
    if list % 2 ==0:
        even+=1
    else:
        odd+=1
print("No. of even : ",even)
print("No. of odd : ",odd)
