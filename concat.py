s = input("please enter the string")
k = int(input("please enter the number :"))
remainder_1 = k%3
remainder_2 = k%5

if remainder_1 == 0:
   
    p =k
elif remainder_2 ==0:
    
    p = k
else:
    p = 0

print( (p+1)*s)
    
