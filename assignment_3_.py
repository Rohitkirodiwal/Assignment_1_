("odd or even no. ")
num = ( 1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0
for num in num:
    if  num %2== 0:
        even+=1
    else:
        odd+=1 
print("no of even : ",even)
print("no of odd : ",odd)