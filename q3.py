import math
num = int(input("enter the no"))
factorial=1
if num<1:
    print("undefined")
elif num==1:
    print("1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)

